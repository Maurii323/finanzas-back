from rest_framework import status   # contiene códigos de estado HTTP comunes
from rest_framework.response import Response    #permite devolver respuestas en formato JSON desde las vistas de la API.
from rest_framework.views import APIView    # Permite crear las APIView para implementar endpoint con logica personalzada
from django.contrib.auth.models import User    # User de django
from rest_framework_simplejwt.tokens import RefreshToken    #se usa para generar y manejar tokens de refresco.
# se usa para autenticar un usuario usando sus credenciales, si devuelve un usuario, significa que las credenciales existen y el login es valido
from django.contrib.auth import authenticate    

# ApiView de registracion
class RegisterView(APIView):
    # Qué debe hacer la vista cuando reciba una solicitud POST
    def post(self, request):
        #Guarda los inputs pasados por el formulario
        username = request.data.get('username')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')
        email = request.data.get('email')

        # Valida si existen los campos y si las contraseñas coinciden
        if not username or not password1 or not password2:
            # Devuelve un error
            return Response({'error': 'Nombre de usuario y las contraseñas son requeridas'}, status=status.HTTP_400_BAD_REQUEST)
        if not password1 == password2:
            return Response({'error': 'Las contraseñas deben coincidir'}, status=status.HTTP_400_BAD_REQUEST)
        # Verificar si el username ya existe
        if User.objects.filter(username=username).exists():
            return Response({'error': 'El nombre de usuario ya existe'}, status=status.HTTP_400_BAD_REQUEST)

        # Crea el lusuario luego de las validaciones y lo guarda
        user = User.objects.create_user(username=username, password=password1, email=email)
        user.save()

        #genera un refresh token y un access token para el usuario proporcionado
        refresh = RefreshToken.for_user(user)
        #Crea una respuesta HTTP que será enviada al cliente
        return Response({
            'refresh': str(refresh),    #Retorna el refresh token
            'access': str(refresh.access_token),    ##Retorna el access token
        }, status=status.HTTP_201_CREATED)
    
# ApiView de Login
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Validación: Verificar que se han enviado las credenciales necesarias
        if not username or not password:
            return Response(
                {'error': 'El nombre de usuario y la contraseña son requeridos'},status=status.HTTP_400_BAD_REQUEST
                )

        # Intentar autenticar al usuario
        user = authenticate(username=username, password=password)
        # Si la autenticacion falló
        if user is None:
            return Response(
                {'error': 'El nombre de usuario o la contraseña son incorrectos '},status=status.HTTP_401_UNAUTHORIZED
                )

        # Generar los tokens si la autenticación es exitosa y los envia con la respuesta HTTP
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)