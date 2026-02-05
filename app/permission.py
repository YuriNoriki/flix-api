from rest_framework import permissions


class GlobalDefaultPermission(permissions.BasePermission):
    """
    Classe de permissão global baseada no model da view.
    Ela converte o método HTTP da requisição (GET, POST, etc.)
    em permissões padrão do Django (view, add, change, delete).
    """

    def has_permission(self, request, view):
        # Obtém dinamicamente o nome da permissão do Django
        # com base no método HTTP e no model associado à view
        model_permission_codename = self.__get_model_permission_codename(
            request.method, view
        )

        # Se não for possível identificar a permissão,
        # o acesso é negado por padrão (segurança)
        if not model_permission_codename:
            return False

        # Verifica se o usuário autenticado possui a permissão
        # Exemplo: 'genres.view_genre'
        return request.user.has_perm(model_permission_codename)

    def __get_model_permission_codename(self, method, view):
        try:
            # Obtém o nome do model associado ao queryset da view
            model_name = view.queryset.model._meta.model_name

            # Obtém o nome da app onde o model está definido
            app_label = view.queryset.model._meta.app_label

            # Converte o método HTTP (GET, POST, etc.)
            # em uma ação de permissão do Django
            action = self.__get_action_suffix(method)

            # Monta o codename da permissão no padrão do Django
            # formato: app_label.action_model
            return f"{app_label}.{action}_{model_name}"

        except AttributeError:
            # Caso a view não possua queryset ou model,
            # a permissão não pode ser determinada
            return None

    def __get_action_suffix(self, method):
        # Mapeia métodos HTTP para ações de permissão do Django
        method_actions = {
            'GET': 'view',       # leitura
            'POST': 'add',       # criação
            'PUT': 'change',     # atualização completa
            'PATCH': 'change',   # atualização parcial
            'DELETE': 'delete',  # exclusão
            'OPTIONS': 'view',   # verificação de rota
            'HEAD': 'view',      # cabeçalho da requisição
        }

        # Retorna a ação correspondente ao método HTTP
        # Se não existir, retorna string vazia
        return method_actions.get(method, '')
