from zoomus import ZoomClient
from django.conf import settings

path('api/create-meeting',views.ZoomMeetingCreateAPIView.as_view()),

path('api/join-meeting',views.ZoomMeetingJoinAPIView.as_view()),


class ZoomAPIClient:
    def __init__(self):
        self.client = ZoomClient(settings.ZOOM_API_KEY, settings.ZOOM_API_SECRET)
    
    def create_meeting(self, topic, start_time, duration, host_id):
        return self.client.meeting.create(user_id=host_id, topic=topic, start_time=start_time, duration=duration)
    
    def get_join_url(self, meeting_id, user_name):
        meeting_info = self.client.meeting.get(id=meeting_id)
        if 'code' in meeting_info and meeting_info['code'] == 300:
            # Handle the error response
            error_message = meeting_info['message']
            # Return or handle the error as needed
        else:
            print(meeting_info,'#'*50)
            #join_url = meeting_info['join_url']
            #print(join_url,'#'*50)
            return meeting_info


from .zoom_client  import ZoomAPIClient
from zoomus import ZoomClient

from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime


class ZoomMeetingCreateAPIView(APIView):
    def post(self, request):
        zoom_api_key =  'VfNxb2b5Ta-Ef1wt3fz4JQ'
        zoom_api_secret  = 'nnzclMpmqFiTaTRV0Hko6OUKWdhWFbqK3EBo'

        zoom_client = ZoomClient(api_key=zoom_api_key, api_secret=zoom_api_secret)

        topic = request.data.get('topic')
        start_time_str = request.data.get('start_time')
        duration = request.data.get('duration')
        host_id = request.data.get('host_id')

        # Add seconds to the start_time_str
        start_time_str += ":00"

        # Convert start_time_str to datetime object
        start_time = datetime.strptime(start_time_str, "%Y-%m-%dT%H:%M:%S")

        # Create the meeting using the Zoom API
        meeting_info = zoom_client.meeting.create(user_id=host_id, topic=topic, start_time=start_time, duration=duration)
        return Response(meeting_info, status=status.HTTP_201_CREATED)

        if meeting_info.get('code') == 201:
            # Meeting created successfully
            return Response({'message': 'Meeting created successfully', 'data': meeting_info}, status=201)
        else:
            # Handle the case when meeting creation failed
            error_message = meeting_info.get('message')
            return Response({'error': error_message}, status=500)


class ZoomMeetingJoinAPIView(APIView):
    def post(self, request):
        meeting_id = request.data.get('meeting_id')
        user_name = request.data.get('user_name')

        zoom_client = ZoomAPIClient()
        join_url = zoom_client.get_join_url(meeting_id, user_name)

        return Response({'join_url': join_url},status=status.HTTP_200_OK)





































import requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response

class CreateZoomMeetingView(APIView):
    def post(self, request):
        # Récupérer les paramètres de la réunion à partir de la requête
        meeting_topic = request.data.get('topic')
        # Ajoutez d'autres paramètres selon vos besoins (ex : heure de début, durée, etc.)

        # Préparer les données pour la création de la réunion
        data = {
            'topic': meeting_topic,
            # Ajoutez d'autres données selon vos besoins
        }
        # Effectuer la requête POST vers l'API Zoom pour créer la réunion
        response = requests.post(
            'https://api.zoom.us/v2/users/me/meetings',
            headers={'Authorization': f'Bearer {settings.ZOOM_API_SECRET}'},
            json=data
        )

        # Vérifier le statut de la réponse
        if response.status_code == 201:
            # La réunion a été créée avec succès
            meeting_data = response.json()
            start_url = meeting_data['start_url']
            join_url = meeting_data['join_url']
            return Response({
                'start_url': start_url,
                'join_url': join_url
            })
        else:
            # La création de la réunion a échoué
            return Response({'message': 'Échec de la création de la réunion'}, status=response.status_code)
