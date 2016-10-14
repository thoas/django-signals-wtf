from django.test import TestCase

from signals_wtf.models import Poll, Answer


class ModelsTests(TestCase):
    def test_simple_compute(self):
        poll = Poll.objects.create(question='Weird?')

        Answer.objects.create(poll=poll, text='Yes')

        # refresh
        poll = Poll.objects.get(pk=poll.pk)

        assert poll.answers_count == 1
