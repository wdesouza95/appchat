from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Conversation, Message

class ConversationListView(ListView):
    model = Conversation
    template_name = 'conversas.html'  # Nome do seu template HTML para listar conversas
    context_object_name = 'conversas'

    def get_queryset(self):
        # Recupera as conversas do usuário atual, por exemplo
        return Conversation.objects.filter(participants=self.request.user)

class ConversationDetailView(DetailView):
    model = Conversation
    template_name = 'conversando.html'  # Nome do seu template HTML para detalhes de conversa
    context_object_name = 'conversation'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        conversation = self.get_object()
        context['messages'] = Message.objects.filter(conversation=conversation)
        return context

    # Adicione métodos para enviar mensagens, etc., conforme necessário
