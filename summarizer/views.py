from django.shortcuts import render
from django.http import JsonResponse
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class call_model(APIView):

    def get(self, request):
        if request.method == 'GET':
            # sentence is the query we want to get the prediction for
            para = request.GET.get('para')

            summarize_text = summarize(para, ratio=0.5)
            keyword = keywords(para, words=5, lemmatize=True)
            return JsonResponse({'summary': summarize_text, 'keywords': keyword})
