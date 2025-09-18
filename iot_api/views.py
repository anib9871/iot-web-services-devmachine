# iot_api/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.permissions import AllowAny


from .models import (
    MasterDevice, DeviceReadingLog, DeviceAlarmLog, 
    MasterOrganization, MasterParameter, MasterSensor,
    CompassDates, SeUser, SensorParameterLink, DeviceSensorLink, DeviceAlarmCallLog , MasterUOM , MasterCentre , MasterRole , CentreOrganizationLink , MasterUser, UserOrganizationCentreLink,MasterNotificationTime , DeviceCategory
)
from .serializers import (
    MasterDeviceSerializer, DeviceReadingLogSerializer, DeviceAlarmLogSerializer,
    MasterOrganizationSerializer, MasterParameterSerializer, MasterSensorSerializer,
    CompassDatesSerializer, SeUserSerializer, SensorParameterLinkSerializer,
    DeviceSensorLinkSerializer, DeviceAlarmCallLogSerializer , MasterUOMSerializer , MasterCentreSerializer , MasterRoleSerializer , CentreOrganizationLinkSerializer,MasterUserSerializer,UserOrganizationCentreLinkSerializer,MasterNotificationTimeSerializer , DeviceCategorySerializer
)


# from .utils import send_sms

# -------------------------
# Login View
# -------------------------
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

# -------------------------
# Logout View
# -------------------------
def logout_view(request):
    logout(request)
    return redirect('login')

def user_dashboard(request):
    return render(request, "user_dashboard.html")

# -------------------------
# Dashboard View
# -------------------------
@login_required
def dashboard_view(request):
    context = {
        'devices_count': MasterDevice.objects.count(),
        'readings_count': DeviceReadingLog.objects.count(),
        'alarms_count': DeviceAlarmLog.objects.count(),
        'organizations_count': MasterOrganization.objects.count(),
        'parameters_count': MasterParameter.objects.count(),
        'sensors_count': MasterSensor.objects.count(),
        'compass_count': CompassDates.objects.count(),
        'users_count': SeUser.objects.count(),
        'sensor_links_count': SensorParameterLink.objects.count(),
        'device_links_count': DeviceSensorLink.objects.count(),
        'alarm_calls_count': DeviceAlarmCallLog.objects.count(),
        'uom_count': MasterUOM.objects.count(),
        'centre_count': MasterCentre.objects.count(),
        'role_count' : MasterRole.objects.count(),
        'centre_links_count': CentreOrganizationLink.objects.count(),
        'master_user_count' : MasterUser.objects.count(),
        'user_organization_centre_link_count': UserOrganizationCentreLink.objects.count(),
        'device_category': DeviceCategory.objects.count(),
    }
    return render(request, 'dashboard.html', context)

# -------------------------
# SMS Test View
# -------------------------
# def some_iot_alert_view(request):
#     try:
#         sms_sid = send_sms('+917355383021', 'Alert! IoT device reading high.')
#         return HttpResponse(f"SMS sent successfully! SID: {sms_sid}")
#     except Exception as e:
#         return HttpResponse(f"Failed to send SMS: {e}")

# -------------------------
# DRF ViewSets for all models
# -------------------------
class MasterDeviceViewSet(viewsets.ModelViewSet):
    queryset = MasterDevice.objects.all()
    serializer_class = MasterDeviceSerializer

class DeviceReadingLogViewSet(viewsets.ModelViewSet):
    queryset = DeviceReadingLog.objects.all()
    serializer_class = DeviceReadingLogSerializer

class DeviceAlarmLogViewSet(viewsets.ModelViewSet):
    queryset = DeviceAlarmLog.objects.all()
    serializer_class = DeviceAlarmLogSerializer

class MasterOrganizationViewSet(viewsets.ModelViewSet):
    queryset = MasterOrganization.objects.all()
    serializer_class = MasterOrganizationSerializer
    permission_classes = [AllowAny]   # 👈 yeh add karo

class MasterParameterViewSet(viewsets.ModelViewSet):
    queryset = MasterParameter.objects.all()
    serializer_class = MasterParameterSerializer

class MasterSensorViewSet(viewsets.ModelViewSet):
    queryset = MasterSensor.objects.all()
    serializer_class = MasterSensorSerializer

class CompassDatesViewSet(viewsets.ModelViewSet):
    queryset = CompassDates.objects.all()
    serializer_class = CompassDatesSerializer

class SeUserViewSet(viewsets.ModelViewSet):
    queryset = SeUser.objects.all()
    serializer_class = SeUserSerializer

class SensorParameterLinkViewSet(viewsets.ModelViewSet):
    queryset = SensorParameterLink.objects.all()
    serializer_class = SensorParameterLinkSerializer

class DeviceSensorLinkViewSet(viewsets.ModelViewSet):
    queryset = DeviceSensorLink.objects.all()
    serializer_class = DeviceSensorLinkSerializer

class DeviceAlarmCallLogViewSet(viewsets.ModelViewSet):
    queryset = DeviceAlarmCallLog.objects.all()
    serializer_class = DeviceAlarmCallLogSerializer

class MasterUOMViewSet(viewsets.ModelViewSet):
    queryset = MasterUOM.objects.all()
    serializer_class = MasterUOMSerializer

class MasterCentreViewSet(viewsets.ModelViewSet):
    queryset = MasterCentre.objects.all()
    serializer_class = MasterCentreSerializer

class MasterRoleViewSet(viewsets.ModelViewSet):
    queryset = MasterRole.objects.all()
    serializer_class = MasterRoleSerializer

class CentreOrganizationLinkViewSet(viewsets.ModelViewSet):
    queryset = CentreOrganizationLink.objects.all()
    serializer_class = CentreOrganizationLinkSerializer

class MasterUserViewSet(viewsets.ModelViewSet):
    queryset = MasterUser.objects.all()
    serializer_class = MasterUserSerializer

class UserOrganizationCentreLinkViewSet(viewsets.ModelViewSet):
    queryset = UserOrganizationCentreLink.objects.all()
    serializer_class = UserOrganizationCentreLinkSerializer

class MasterNotificationTimeViewSet(viewsets.ModelViewSet):
    queryset = MasterNotificationTime.objects.all()
    serializer_class = MasterNotificationTimeSerializer

class DeviceCategoryViewSet(viewsets.ModelViewSet):
    queryset = DeviceCategory.objects.all()
    serializer_class = DeviceCategorySerializer