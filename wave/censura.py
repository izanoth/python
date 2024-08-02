
import wave

class CensorClip:
    def __init__(self, duration_seconds=1):
        self.duration_seconds = duration_seconds
        self.sample_rate = 44100
        self.amplitude = 32767
        self.censor_wave = None

    def create_censor_beep(self):
        self.censor_wave = wave.open("censor_beep.wav", 'w')
        self.censor_wave.setparams((1, 2, self.sample_rate, 0, 'NONE', 'not compressed'))

        for i in range(int(self.sample_rate * self.duration_seconds)):
            sample = int(self.amplitude * 0.5)
            self.censor_wave.writeframesraw(sample.to_bytes(2, byteorder='little'))

    def save_censor_clip(self, filename):
        if self.censor_wave is not None:
            self.censor_wave.close()
            with open(filename, 'wb') as f:
                with open('censor_beep.wav', 'rb') as g:
                    f.write(g.read())

# Criar e salvar o clip de censura
censor_clip = CensorClip(duration_seconds=6)  # Altere a duração conforme necessário
censor_clip.create_censor_beep()
censor_clip.save_censor_clip("censor_beep_extended.wav")  # Nome do arquivo de saída
