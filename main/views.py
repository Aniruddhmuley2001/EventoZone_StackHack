from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Event, Participant
from django.contrib import messages
from twilio.rest import Client
from django.utils import timezone
from eventozone import settings
from django.core.mail import send_mail
import datetime


def root(request):
    return redirect('index')

def index(request):
    return render(request, 'index.html')

def test(request):
    return render(request, 'test.html')

def eventReg(request):
    if request.method == 'POST':
        event = Event(
            Name = request.POST["e_name"],
            Description = request.POST["e_desc"],
            Location = request.POST["e_location"],
            fromDate = request.POST["e_fdate"],
            fromTime = request.POST["e_ftime"],
            toDate = request.POST["e_tdate"],
            toTime = request.POST["e_ttime"],
            regEndDate = request.POST["e_rdate"],
            regEndTime = request.POST["e_rtime"],
            posterLink = request.POST["e_poster"],
            hostEmail = request.POST["e_email"],
            hostPW = request.POST["e_pw"]
            )
        event.save()
        subject = 'Event Registration Successful'
        msg = 'Thank you for registering your event with us.'\
            + '\n\nEvent Name: ' + request.POST["e_name"]\
            + '\nEvent ID: ' + str(Event.objects.get(Name=request.POST["e_name"]).id)\
            + '\n\nYou can now review the participation in your event through our portal.'\
            + '\n\nTeam EventoZone'
        to = request.POST["e_email"]
        send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
        return redirect('index')
    else:
        return render(request, 'eventReg.html')


def eventDash(request):
    if request.method == 'POST':
        id = request.POST["event_id"]
        pw = request.POST["event_pw"]
        if Event.objects.filter(id=id).exists():
            if Event.objects.get(id=id).hostPW == pw:
                participants = Participant.objects.filter(EventID = id)
                contents = {
                    'participants' : participants,
                    'flag' : 1
                }
                return render(request, 'eventDash.html', contents)
            else:
                messages.info(request, 'Incorrect Password!')
                return render(request, 'evenDash.html')
        else:
            messages.info(request, 'No event is registered with this Event-ID.')
            return render(request, 'evenDash.html')
    else:
        contents = {
            'flag' : 0
        }
        return render(request, 'eventDash.html', contents)


def participantReg(request):
    if request.method == 'POST':
        participant = Participant(
            Name = request.POST["p_name"],
            Contact = request.POST["p_contact"],
            Email = request.POST["p_email"],
            proofLink = request.POST["p_proof"],
            Type = request.POST["p_type"],
            Tickets = request.POST["p_tickets"],
            EventID = request.POST["p_event"]
            )
        if (Participant.objects.filter(Email=request.POST["p_email"]).exists() and Participant.objects.get(Email=request.POST["p_email"]).EventID==int(request.POST["p_event"])):
            messages.info(request, 'You have already registered for this event.')
            return redirect('participantReg')
        else:
            participant.save()
            event = Event.objects.get(id=request.POST["p_event"])

            
            # ---------- IMPORTANT:
            # The following peices of code are commented as these are yet in the development phase.
            # It requires various accounts credentials that can be set up later.
            # DEMO OF THIS PART IS AVAILABLE IN THE PROJECT SUBMISSION.


            # ------------------------- code for E-Mail notifications -------------------------

            # subject = 'Event Registration Successful'
            # msg = 'Thank you ' + request.POST["p_name"] + ' for registering your participation with us.'\
            #     + '\n\nParticipant-ID: ' + str(participant.id)\
            #     + '\nEvent Name: ' + event.Name\
            #     + '\nLocation: ' + event.Location\
            #     + '\nDate(s): ' + str(event.fromDate) + ' - ' + str(event.toDate)\
            #     + '\nTime: ' + str(event.fromTime) + ' - ' + str(event.toTime)\
            #     + '\nParticipation Type: ' + request.POST["p_type"]\
            #     + '\nNo. of people: ' + request.POST["p_tickets"]\
            #     + '\n\n\nTeam EventoZone'
            # to = request.POST["p_email"]
            # send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])

            # ------------------------- code for Mobile Message notifications -------------------------

            # account_sid = '------------------------------'
            # auth_token = '------------------------------'
            # client = Client(account_sid, auth_token)
            # client.messages.create(
            #                         from_='--------------',
            #                         to='+91' + request.POST["p_contact"],
            #                         body='Thank you ' + request.POST["p_name"] + ' for registering your participation with us.'
            #                             + '\n\nParticipant-ID: ' + str(participant.id)
            #                             + '\nEvent Name: ' + event.Name
            #                             + '\nLocation: ' + event.Location
            #                             + '\nDate(s): ' + str(event.fromDate) + ' - ' + str(event.toDate)
            #                             + '\nTime: ' + str(event.fromTime) + ' - ' + str(event.toTime)
            #                             + '\nParticipation Type: ' + request.POST["p_type"]
            #                             + '\nNo. of people: ' + request.POST["p_tickets"]
            #                             + '\n\n\nTeam EventoZone'
            #                        )
            return redirect('index')
    else:
        currDate = datetime.datetime.now().date()
        currTime = datetime.datetime.now().time()
        for obj in Event.objects.all():
            if obj.regEndDate >= currDate:
                if obj.regEndTime > currTime:
                    continue
                else:
                    obj.status = 0
                    obj.save()
            else:
                obj.status = 0
                obj.save()

        contents = {
            'events' : Event.objects.all(),
            'currDate' : currDate,
            'currTime' : currTime
        }
        return render(request, 'participantReg.html', contents)