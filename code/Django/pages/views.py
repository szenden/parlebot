from django.shortcuts import render



def home(request):
	return render(request, "home.html", {})

def about(request):
	return render(request, "about.html", {})

def questions(request):
	return render(request, "questions.html", {})

def kamerstukken(request):
	return render(request, "kamerstukken.html", {})

def kamerstukken_minister(request):
	return render(request, "kamerstukken_minister.html", {})

def kamervragen_beantwoorden(request):
	return render(request, "kamervragen_beantwoorden.html", {})

def kamervragen_antwoorden_bekijken(request):
	return render(request, "kamervragen_antwoorden_bekijken.html", {})	

def parlementarier_portaal(request):
	return render(request, "parlementarier_portaal.html", {})	

def minister_portaal(request):
	return render(request, "minister_portaal.html", {})	

def login(request):
	return render(request, "login.html", {})

def wachtwoord_vergeten(request):
	return render(request, "wachtwoord_vergeten.html", {})			

def wachtwoord_reset(request):
	return render(request, "wachtwoord_reset.html", {})	

def parlementarier_kamervragen_stellen(request):
	return render(request, "parlementarier_kamervragen_stellen.html", {})		

def parlementarier_kamervragen_bekijken(request):
	return render(request, "parlementarier_kamervragen_bekijken.html", {})	

def kamervragen_versturen(request):
	return render(request, "kamervragen_versturen.html", {})

def kamervragen_antwoorden_a(request):
	return render(request, "kamervragen_antwoorden_a.html", {})	

def kamervragen_antwoorden_b(request):
	return render(request, "kamervragen_antwoorden_b.html", {})	

def kamervragen_antwoorden_versturen(request):
	return render(request, "kamervragen_antwoorden_versturen.html", {})	

def kamervragen_minister_antwoorden(request):
	return render(request, "kamervragen_minister_antwoorden.html", {})	




#in the below section i am testing various database inserts, which will be deleted later on.

def insertform(request):
	return render(request, "insertform.py", {})

def form_test(request):
	print("Form submitted succesfully.")
	return render(request, "form_test.html", {})

def dbconnect(request):
	return render(request, "dbconnect.py", {})

def testdbinput(request):
	print("Form submitted succesfully.")
	return render(request, "testdbinput.py", {})