from django.http import HttpResponse
from django.shortcuts import render


def website(request):
    return HttpResponse('''
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Personal Navigator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }

        header {
            background-color: #4CAF50;
            color: white;
            padding: 10px 0;
            text-align: center;
        }

        nav {
            display: flex;
            justify-content: center;
            background-color: #333;
        }

        nav a {
            color: white;
            padding: 14px 20px;
            text-decoration: none;
            text-align: center;
        }

        nav a:hover {
            background-color: #ddd;
            color: black;
        }

        section {
            padding: 20px;
            margin: 10px;
            border: 1px solid #ddd;
            text-align:center;
        }

        .hero {
            background-color: #f4f4f4;
            padding: 50px;
            text-align: center;
        }

        .about, .services, .contact {
            background-color: #fff;
        }

        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 10px 0;
            position: fixed;
            width: 100%;
            bottom: 0;
        }
        @media (max-width: 600px) {
            nav {
                flex-direction: column;
            }
            nav a {
                padding: 10px;
            }
        }
    </style>
</head>
<body>

<header>
    <h1>Welcome to MIK</h1>
</header>

<nav>
    <a href="http://127.0.0.1:8000/action">Action</a>
</nav>

<section id="home" class="hero">
    <h2>Punctuation Remover</h2>
    <p>In this section, Enter a line or paragraph to remove punctuation.</p>
</section>
<section id="about" class="Capitalize First">
    <h2>Capitalize Whole</h2>
    <p>In this section, Enter a line or word to make it Capitalize.</p>
</section>

<section id="about" class="Capitalize First">
    <h2>Capitalize First</h2>
    <p>In this section, Enter a line or word to make its first character Capitalize.</p>
</section>

<section id="services" class="services">
    <h2>New Line Remover</h2>
    <p>In this section, Enter a line or para to remove New Line.</p>
</section>

<section id="contact" class="contact">
    <h2>Space Remover</h2>
    <p>In this section, Enter a line or para to remove Spaces.</p>
</section>
<br>

<footer>
    <p>&copy; MIK. All rights reserved.</p>
</footer>

</body>
</html>
')''')


def Action(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the text
    dj_text = request.POST.get("text", 'default')

    # Check checkbox values
    remove_punc = request.POST.get("remove_Punc", "off")
    upper_response = request.POST.get("uppercase", "off")
    capt_first = request.POST.get("capt_first", "off")
    new_line = request.POST.get("new_line", "off")
    extra_spaces = request.POST.get("extra_spaces", "off")

    # Initialize analyzed_text with the input text
    analyzed_text = dj_text

    # Remove punctuations
    if remove_punc == "on":
        punctuations = '''!()-[]{};:'\,"<>./?@#$%^&*_~'''
        analyzed_text = "".join(char for char in analyzed_text if char not in punctuations)
        # analyzed_text = analyzed_text.replace(" ", "")

    # Convert to uppercase
    if upper_response == "on":
        analyzed_text = analyzed_text.upper()
        analyzed_text = analyzed_text.replace(" ", "")

    if new_line == "on":
        analyzed = ""
        for char in analyzed_text:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        analyzed_text = analyzed

    if capt_first == "on":
        analyzed_text = analyzed_text.capitalize()
        analyzed_text = analyzed_text.replace(" ", "")

    if extra_spaces == "on":
        analyzed = ""
        for ind, char in enumerate(analyzed_text):
            if not(analyzed_text[ind] == " " and dj_text[ind + 1] == " "):
                analyzed = analyzed + char
        analyzed_text = analyzed
    params = {
        "purpose": "Text Analysis",
        "analyzed_text": analyzed_text,
        "length": len(analyzed_text)
    }

    return render(request, 'analyze.html', params)
