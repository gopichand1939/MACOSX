from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Carousel, HomeIntro, ClientLogo
from .serializers import CarouselSerializer
from rest_framework import generics
from .serializers import CarouselSerializer, HomeIntroSerializer, ClientLogoSerializer

@method_decorator(csrf_exempt, name='dispatch')
class CarouselAPIView(APIView):
    """
    GET: Fetch all carousel entries.
    POST: Create a new carousel entry.
    """
    permission_classes = [permissions.AllowAny]  # Switch to IsAuthenticated in production

    def get(self, request, format=None):
        carousels = Carousel.objects.all()
        serializer = CarouselSerializer(carousels, many=True)
        return Response({"carousel": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = CarouselSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"carousel": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class CarouselUpdateAndDeleteView(APIView):
    """
    Retrieve, update or delete a carousel instance.
    """
    def get_object(self, pk):
        try:
            return Carousel.objects.get(pk=pk)
        except Carousel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CarouselSerializer(snippet)
        return Response({"carousel": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CarouselSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"carousel": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





   
class ClientCarouselView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer

    """
    List all carousel, or create a new carousel.
    """

    def get(self, request, format=None):
        snippets = Carousel.objects.all()
        serializer = CarouselSerializer(snippets, many=True)
        return Response({"carousel": serializer.data}, status=status.HTTP_200_OK)

'''
    ------------------------------------------------ Home intro section ------------------------------------------------------
'''
class HomeIntroAPIView(generics.CreateAPIView):
     permission_classes = [permissions.IsAuthenticated]
     serializer_class = HomeIntroSerializer
     queryset = HomeIntro.objects.all()

     """
     List all intro, or create a new Intro.
     """

     def get(self, request, format=None):
        snippets = HomeIntro.objects.all()
        serializer = HomeIntroSerializer(snippets, many=True)
        return Response({"intro": serializer.data}, status=status.HTTP_200_OK)
    
     def post(self, request, format=None):
        serializer = HomeIntroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"intro": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     


class HomeIntroUpdateAndDeleteView(APIView):
    """
    Retrieve, update or delete a carousel instance.
    """
    def get_object(self, pk):
        try:
            return HomeIntro.objects.get(pk=pk)
        except HomeIntro.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = HomeIntroSerializer(snippet)
        return Response({"intro": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = HomeIntroSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"intro": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


   
class ClientHomeIntroView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = HomeIntro.objects.all()
    serializer_class = HomeIntroSerializer

    """
    List all carousel, or create a new carousel.
    """

    def get(self, request, format=None):
        snippets = HomeIntro.objects.all()
        serializer = HomeIntroSerializer(snippets, many=True)
        return Response({"intro": serializer.data}, status=status.HTTP_200_OK)
    
'''
    ------------------------------------------------ Client Images section ------------------------------------------------------
'''


class ClientLogoAPIView(generics.CreateAPIView):
     permission_classes = [permissions.IsAuthenticated]
     serializer_class = ClientLogoSerializer
     queryset = ClientLogo.objects.all()

     """
     List all ClientLogo, or create a new ClientLogo.
     """

     def get(self, request, format=None):
        snippets = ClientLogo.objects.all()
        serializer = ClientLogoSerializer(snippets, many=True)
        return Response({"clientLogo": serializer.data}, status=status.HTTP_200_OK)
    
     def post(self, request, format=None):
        serializer = ClientLogoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"clientLogo": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ClientLogoUpdateAndDeleteView(APIView):
    """
    Retrieve, update or delete a carousel instance.
    """
    def get_object(self, pk):
        try:
            return ClientLogo.objects.get(pk=pk)
        except ClientLogo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ClientLogoSerializer(snippet)
        return Response({"clientLogo": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ClientLogoSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"clientLogo": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


   
class ClientLogoImagesView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = ClientLogo.objects.all()
    serializer_class = ClientLogoSerializer

    """
    List all ClientLogo, or create a new ClientLogo.
    """

    def get(self, request, format=None):
        snippets = ClientLogo.objects.all()
        serializer = ClientLogoSerializer(snippets, many=True)
        return Response({"clientLogo": serializer.data}, status=status.HTTP_200_OK)