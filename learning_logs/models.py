from django.db import models


class Topic(models.Model):
    """Um assunto sobre o qual o usuário está aprendendo."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        """Desenvolve uma representação em string do modelo."""
        return self.text


class Entry(models.Model):
    """Algo específico aprendido sobre um assunto."""
    # Adicionado on_delete=models.PROTECT (ou CASCADE) para essa 
    # versão atual do Django (16/01/2020 - 3.0.2)
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        verbose_name_plural = 'entries'


    def __str__(self):
        """Devolve uma representação em string do modelo."""
        # 18.2 - Entradas menores: Acrescente um if no método __str__
        # que adicione reticências somente se a entrada tiver mais de 
        # 50 caracteres. Adicionar no site de administração uma entrada
        # com menos de 50 caracteres
        
        if len(self.text) >= 50:
            return str(self.text)[:50] + "..."
        else:
            return str(self.text)
