{% load static %}
<!doctype html>

<link href="{% static 'css/style.css' %}" rel="stylesheet" type="text/css" media="all">

<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

    <link rel="shortcut icon" href="{% static 'images/favicons.ico' %}">

    <title>{% block title %}Parlebot{% endblock %}</title>

<div class="container head">
  <div class="row">

    <div class="header_logo">
      <a href="{% url 'home' %}">
        <img src="{% static 'images/logo.jpg' %}" alt="Naar de homepage van Rijksoverheid.nl" id="logotweedekamer">
      </a>
    </div>

    <div class="wrapper box">
      <form class="form-inline">
        <p class="header_language" type="text">English</p>
      <input class="form-control mr-sm-2 header_search" type="search" placeholder="Zoeken" aria-label="Search">
    </form>
    </div>
    <div class="login_profile">
      <a href="{% url 'login' %}">
        <img id="login_profile_image" src="{% static 'images/login_profile_image.png' %}"></a>
    </div>
    <div class=login_profile_text>
    <a id="login_profile_text" href="{% url 'login' %}" style="color: #121469;">Login</a>
  </div>
  </div>
</div>
 <nav class="navbar navbar-expand-lg navbar-white bg-white" style="padding-left: 400px;">
  <!--<a class="navbar-nav" href="#"style="color: #121469;">Debat en vergadering
  <img id="down-arrow" src="{% static 'images/down-arrow.png' %}" alt="Naar de homepage van Rijksoverheid.nl" id="logotweedekamer"></a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button> -->

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="{% url 'home' %}" style="color: #121469;"> Debat en vergadering
          <img id="down-arrow" src="{% static 'images/down-arrow.png' %}"><span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="{% url 'home' %}" style="color: #121469;"> Kamerleden en commisies
          <img id="down-arrow" src="{% static 'images/down-arrow.png' %}"><span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="{% url 'kamerstukken' %}"style="color: #FFF; background-color: #121469; ">Kamerstukken
          <img id="down-arrow" src="{% static 'images/down-arrow-white.png' %}"></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="{% url 'questions' %}"style="color: #121469; ">Zo werkt de kamer 
        <img id="down-arrow" src="{% static 'images/down-arrow.png' %}"></a>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link" style="color: #121469; padding-left: 100px;" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Contact en bezoek
          <img id="down-arrow" src="{% static 'images/down-arrow.png' %}"></a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
          <a class="dropdown-item" href="#">Action</a>
          <a class="dropdown-item" href="#">Another action</a>
          <div class="dropdown-divider"></div>
          <a class="dropdown-item" href="#">Something else here</a>
        </div>
      </li>
    </ul>
  </div>
</nav>
  </head>

  <body class="body">
  

    {% block content %}

    {% endblock %}

 
<br/><br/>
<!--<center><small>Copyright &copy; Parlebot.com - All Rights Reserved</small></center> -->
<footer class="layout_footer tk_v2">
      <div class="footer">
        <div class="footer_container">
           <div class="row_footer">
            <div class="footer_placement">
            <ul>
              <p class="footer_title">
              <a href="#">Over Tweedekamer.nl</a>
            </p>
              <li>
                <a href="#" class="footer_link">Colofon</a>
              </li>
               <li>
                <a href="#">Disclaimer</a>
              </li>
               <li>
                <a href="#">Uw privacy</a>
              </li>
               <li>
                <a href="#">Toegankelijkheid</a>
              </li>
               <li>
                <a href="#">Sitemap</a>
              </li>
            </ul>
            </div>

            <div class="footer_placement">
            <ul>
              <p class="footer_title">
              <a href="#">Blijf op de hoogte</a>
            </p>
              <li>
                <a href="#" class="footer_link">Twitter</a>
              </li>
               <li>
                <a href="#">Instagram</a>
              </li>
               <li>
                <a href="#">Facebook</a>
              </li>
               <li>
                <a href="#">Facebookpagina Voorzitter</a>
              </li>
               <li>
                <a href="#">E-mailattenderingen</a>
              </li>
              <li>
                <a href="#">Debat Direct</a>
              </li>
            </ul>
            </div>

            <div class="footer_placement">
            <ul>
              <p class="footer_title">
              <a href="#">Ambtelijke ondersteuning</a>
            </p>
              <li>
                <a href="#" class="footer_link">Organogram</a>
              </li>
               <li>
                <a href="#">Werken bij de Tweede Kamer</a>
              </li>
            </ul>
            </div>

            <div class="footer_placement">
            <ul>
              <p class="footer_title">
              <a href="#">Links</a>
            </p>
              <li>
                <a href="#" class="footer_link">Politieje websitees</a>
              </li>
               <li>
                <a href="#">De Tweede Kamer aan het werk</a>
              </li>
               <li>
                <a href="#">De Derde Kamer</a>
              </li>
               <li>
                <a href="#">Debat gemist</a>
              </li>
               <li>
                <a href="#">Open Data Portaal</a>
              </li>
            </ul>
            </div>

          </div>
        </div>
      </div>
</div>
   </footer>
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
  </body>
</html>