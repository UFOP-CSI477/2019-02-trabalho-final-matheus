from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Poll(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default = 1)
    texto = models.CharField(max_length = 255)
    pub_date = models.DateField(null = True, blank = True)

    def __str__(self):
        return self.texto        
    def user_can_vote(self, user):
        """
        Retorna False se o usuário já tiver votado em um votacao, caso contrário, retorna True
        """

        user_votes = user.vote_set.all()
        qs = user_votes.filter(poll=self)
        if qs.exists():
            return False
        return True

    @property
    def num_votes(self):
        return self.vote_set.count()

    def get_results_dict(self):

        res = []
        for choice in self.choice_set.all():
            d = {}
            d['text'] = choice.opcao_escolha
            d['num_votes'] = choice.num_votes
            if not self.num_votes:
                d['percentage'] = 0
            else: 
                d['percentage'] = choice.num_votes / self.num_votes * 100
            res.append(d)
        return res


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete = models.CASCADE)
    opcao_escolha = models.CharField(max_length = 255)

    def __str__(self):
        return "{} - {}".format(self.poll.texto[:25], self.opcao_escolha[:25])

    @property
    def num_votes(self):
        return self.vote_set.count()


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete= models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete = models.CASCADE)
