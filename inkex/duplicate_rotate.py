import inkex
from inkex import load_svg

class DuplicateAndRotate(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)

        # Define os argumentos de linha de comando com argparser
        self.arg_parser.add_argument("--iterations", type=int, default=10, help="Number of iterations")
        self.arg_parser.add_argument("--angle", type=float, default=30, help="Rotation angle in degrees")

    def effect(self):
        # Obtenha os valores dos argumentos de linha de comando
        iterations = self.options.iterations
        angle = self.options.angle

        # Carregue o documento SVG
        svg = self.load_svg('mandala.svg')

        # Encontre o 'g' elemento com id 'layer1'
        selected = svg.find(".//{http://www.w3.org/2000/svg}g[@id='layer1']")

        if selected is not None:
            # Duplicar e rotacionar o elemento 'g' selecionado
            for i in range(iterations):
                duplicate = selected.copy()
                duplicate.set("transform", f"rotate({angle * i})")
                svg.append(duplicate)

        # Salvar o SVG modificado
        self.write_svg('output.svg')

if __name__ == '__main__':
    effect = DuplicateAndRotate()
    effect.run()
