from django.db import models
from datetime import datetime

# Create your models here.
class Pilot(models.Model):
    name = models.CharField(max_length=200)
    weight = models.DecimalField('weight', max_digits=4, decimal_places=1)
    dob = models.DateTimeField('dob')
    pub_date = models.DateTimeField('date published',default=datetime.now)
    def __str__(self):
        return self.name

class Aircraft(models.Model):
    tail_number = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    ac_type = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    serial_no = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published',default=datetime.now)
    def __str__(self):
        return self.tail_number

class Airport(models.Model):
    full_name = models.CharField(max_length=200)
    identifier = models.CharField(max_length=5)
    elevation = models.IntegerField('elevation')
    pub_date = models.DateTimeField('date published',default=datetime.now)
    def __str__(self):
        return self.identifier

class Mission(models.Model):
    mission_name = models.TextField(default='mission_name')
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    starting_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='starting_airport')
    destination_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='destination_airport')
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    notes = models.TextField('notes')
    start_time = models.DateTimeField('start time')
    end_time = models.DateTimeField('end time')
    pub_date = models.DateTimeField('date published',default=datetime.now)
    def __str__(self):
        return self.mission_name

#Individual Flight Data Node
class Flightdata(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    x_accel = models.DecimalField('X-axis acceleration', max_digits=12, decimal_places=6)
    y_accel = models.DecimalField('Y-axis acceleration', max_digits=12, decimal_places=6)
    z_accel = models.DecimalField('Z-axis acceleration', max_digits=12, decimal_places=6)
    x_gyro = models.DecimalField('X-axis rate gyro', max_digits=12, decimal_places=6)
    y_gyro = models.DecimalField('Y-axis rate gyro', max_digits=12, decimal_places=6)
    z_gyro = models.DecimalField('Z-axis rate gyro', max_digits=12, decimal_places=6)
    heading = models.DecimalField('heading', max_digits=12, decimal_places=6)
    course = models.DecimalField('course', max_digits=12, decimal_places=6)
    magnetic_heading = models.DecimalField('magnetic heading', max_digits=12, decimal_places=6)
    alt = models.DecimalField('altitude', max_digits=12, decimal_places=6)
    pressure = models.DecimalField('pressure', max_digits=12, decimal_places=6)
    gps_time_delta = models.DateTimeField('time from gps signal')
    gps_time = models.DateTimeField('gps time')
    pub_date = models.DateTimeField('date published')
