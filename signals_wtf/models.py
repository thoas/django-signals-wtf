from django.db import models
from django.db.models import signals


class Poll(models.Model):
    question = models.CharField(max_length=255)
    answers_count = models.PositiveIntegerField(default=0)


class AnswerManager(models.Manager):
    def contribute_to_class(self, cls, name):
        signals.post_save.connect(self.post_save, sender=cls)

        return super(AnswerManager, self).contribute_to_class(cls, name)

    def post_save(self, instance, **kwargs):
        poll = instance.poll
        poll.answers_count = poll.answers.count()
        poll.save(update_fields=('answers_count', ))


class Answer(models.Model):
    text = models.CharField(max_length=255)
    poll = models.ForeignKey(Poll, related_name='answers')
