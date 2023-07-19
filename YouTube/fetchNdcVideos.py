import scrapetube

videos = scrapetube.get_channel("UCTdw38Cw6jcm0atBPA39a0Q")
for video in videos:
    videoId = video['videoId']
    published = video['publishedTimeText']['simpleText']
    title = video['title']['runs'][0]['text']
    lenght_text = video['lengthText']['simpleText']
    lenght_minutes = 0
    url = video['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url']
    print(f"{videoId} = {published} = {title} = {lenght_text} = {lenght_minutes} = https://youtube.com{url}")

output = """
AYU0vw6IyUY = 4 days ago = Make a great-looking 3D landscape visualization! - Kristoffer Dyrkorn - NDC Oslo 2023 = 59:06
1K1LRzXeO_4 = 5 days ago = OpenAPI & .NET: You're Doing It Wrong - Mark Rendle - NDC Oslo 2023 = 57:15
iDWwoz9ZUzw = 5 days ago = Design Good Schemas - Get a Better Database - Nuri Halperin - NDC Oslo 2023 = 1:02:19
I2NqMbKc8K4 = 5 days ago = God really plays dice - Introduction to Quantum Computing with Q# - Filip w - NDC Oslo 2023 = 56:34
cae0jXRrNno = 5 days ago = Let's Get Scary and Continuously Deploy Database Changes! - Dan Mallott - NDC Oslo 2023 = 1:00:00
vXLz_U4xzkc = 5 days ago = How AI is impacting cybersecurity. Does it? - Victoria Almazova - NDC Oslo 2023 = 52:36
Nyj2O8gHJZM = 5 days ago = Developing an intersectional framework to analyze biases in artificial intelligence and deep neural = 22:37
hj2yFugmpz8 = 5 days ago = How to choose the right database for your application - Zoe Steinkamp - NDC Oslo 2023 = 41:03
qYH1NNmF2hk = 6 days ago = The state of passwordless auth on the web - Phil Nash - NDC Oslo 2023 = 50:30
LR7lprNsR_A = 6 days ago = Immersive storytelling with code, graphics and wit - Einar Otto Stangvik & Jonas Nilsson = 53:38
U8Aame0akl4 = 6 days ago = Message processing failed! But what's the root cause? - Laila Bougria - NDC Oslo 2023 = 55:27
Av2OrTgEh-g = 6 days ago = Securing your app's communications with Kubernetes, Azure Key Vault, and TLS certificates - Eugene = 15:12
wPeUhC-EOys = 7 days ago = Robi - a programming game for kids - Ruth Merethe Granevang - NDC Oslo 2023 = 10:40
7Tq9s_A9CoU = 7 days ago = Prometheus 101 - Nils Otto Johansen - NDC Oslo 2023 = 16:10
DPzOHZNdluA = 7 days ago = Design systems and how to use it - Kitty Toft - NDC Oslo 2023 = 12:31
NuzCoPxedMU = 7 days ago = Sessionize: From idea to 100.000 speakers, and beyond! - Domagoj Pavlešić - NDC Oslo 2023 = 51:14
ZsE_lHjx9vM = 7 days ago = Architecting a secure cloud framework - Sarah Young - NDC Oslo 2023 = 50:21
y5i6VlfQVN4 = 7 days ago = Debugging Difficult Conversations - Or "How not to chicken out" - Andrew Murphy - NDC Oslo 2023 = 56:56
545Nj0_BuzA = 10 days ago = Real-world examples on optimizing .NET performance - Stefán Jökull Sigurðarson - NDC Oslo 2023 = 40:18
Lw04HRF8ies = 10 days ago = CQRS pitfalls and patterns - Udi Dahan - NDC Oslo 2023 = 59:26
Ga6LlDvkXvs = 10 days ago = Principles and Practices of Building Machine Learning Systems - Camilla Montonen - NDC Oslo 2023 = 47:34
dzte-Q0NTdg = 10 days ago = Common Query Patterns in MQL (Mongo Query Language) - Nuri Halperin - NDC Oslo 2023 = 59:12
aMd1FYxaJDY = 10 days ago = Did I break prod? - Ewelina Wilkosz - NDC Oslo 2023 = 40:58
w9QUvZxIpcE = 10 days ago = AI language models in journalism - Andre Voigt - NDC Oslo 2023 = 12:53
K3IqyhKymXc = 10 days ago = 5 reasons to start a book club - Marion Løken - NDC Oslo 2023 = 12:59
ZozbJ_5SIAk = 11 days ago = Tracking Aircraft with Redis & Software-Defined Radio - Guy Royse - NDC Oslo 2023 = 54:52
SAWVPCO575k = 11 days ago = Modelling vs Reality - Einar Høst  - NDC Oslo 2023 = 54:19
9AanhFsM0cE = 11 days ago = Introduction to Serverless with .NET + AWS Lambda - Brandon Minnick - NDC Oslo 2023 = 51:30
Yu4kIgAH_NM = 11 days ago = Clean Code: Be The Hero - Ben Dechrai - NDC Oslo 2023 = 42:56
uNGDW3snVyA = 11 days ago = Bun, Deno, Node.js? Recreating a JavaScript runtime from Scratch - Erick Wendel - NDC Oslo 2023 = 48:54
33fpZNIVHh8 = 11 days ago = Real-time Fraud Detection Challenges and Solutions - Fawaz Ghali - NDC Oslo 2023 = 47:12
5A22s_QXTRg = 11 days ago = How complex software impacts your cognitive abilities - Corstian Boerman - NDC Oslo 2023 = 46:39
fi9P3-7VqHo = 12 days ago = .NET Systems Programming Learned the Hard Way - Aaron Stannard - NDC Oslo 2023 = 1:05:54
WtUCZYyv-_w = 12 days ago = Git Hidden Gems - Enrico Campidoglio - NDC Oslo 2023 = 59:12
UI2FNPoBTGo = 12 days ago = Working with Vue 3.0 and ASP.NET Minimal API - Rob Conery - NDC Oslo 2023 = 1:00:31
BfYxZ4mfv0E = 12 days ago = Let's Code an incremental source generator with Roslyn - Stefan Pölz - NDC Oslo 2023 = 59:50
Bk2nmX13etQ = 12 days ago = The Empowered Software Engineer - unlocking engineering potential - Martin Mazur - NDC Oslo 2023 = 1:00:25
yPxZsF5UpZk = 12 days ago = Not having conflicts is not an option… let’s have good ones - Marion Løken - NDC Oslo 2023 = 57:10
atYHKU0VJQE = 12 days ago = Imposter Syndrome: Overcoming Self-Doubt in Success - Heather Downing - NDC Oslo 2023 = 47:38
9t0EyJ3wPpM = 13 days ago = How hacking works - Web edition - Espen Sande-Larsen - NDC Oslo 2023 = 1:00:59
GrcanQ-nT_s = 13 days ago = Falling off the Edge: Practical Uses for Edge Computing - Alexander Karan - NDC Oslo 2023 = 44:46
ikVmos28Vk0 = 13 days ago = Kotlin - The Chronicles of Lost Semicolons - Christian Woerz - NDC Oslo 2023 = 50:15
ctTJaEI7bSY = 13 days ago = Zen and the Art of Code Life Cycle Maintenance - Phil Nash - NDC Oslo 2023 = 55:20
0wcUG2EV-7E = 13 days ago = An Introduction to Residuality Theory - Barry O'Reilly - NDC Oslo 2023 = 52:55
S3kM2e7UHIs = 13 days ago = A Brief History of Computer Music - Anders Norås - NDC Oslo 2023 = 52:59
2UHYr1tuBFs = 13 days ago = Kubernetes Resiliency - Chris Ayers - NDC Oslo 2023 = 44:54
jnFbMZoP6Ug = 2 weeks ago = Testing strategy for your ASP.NET Core micro-service - Dror Helper - NDC Oslo 2023 = 58:13
Q2Kp4m-FzfQ = 2 weeks ago = A Brief History of Data Storage - Eli Holderness - NDC Olso 2023 = 1:00:11
spgivXIYC04 = 2 weeks ago = Leadership Through Self-Awareness - Melissa Houghton - NDC Oslo 2023 = 49:41
YmH-9BcH1CY = 2 weeks ago = Build a Secure Developer Platform Using Argo, Istio and Vault - Jona Apelbaum & Allessandro Vozza = 58:43
AEwRMRJksJ0 = 2 weeks ago = Training a PowerPoint AI to Play Tic Tac Toe - Brenton Adey - NDC Oslo 2023 = 48:06
s1RSVGKDpcU = 2 weeks ago = Reinventing Visio in 2023, A Blazor Project - Stephen Strong - NDC Oslo 2023 = 55:39
n0c3Pn9Cx5Y = 2 weeks ago = Introducing the Windows App SDK - Nico Vermeir - NDC Oslo 2023 = 1:03:12
IXCZAFwT5GY = 2 weeks ago = Running ASP.NET Core Apps without a server? WHAT??? - Isaac Levin - NDC Oslo 2023 = 46:23
Dr2Sx3fQ-8Y = 2 weeks ago = Emerging threats against cloud application identities and what you should do about it - Sarah Young = 55:52
pEUO9Sj68hg = 2 weeks ago = NOPASSWD: Building a Passwordless Cloud Infrastructure - Kyle Kotowick - NDC Oslo 2023 = 40:01
hgWHfNki5AI = 2 weeks ago = What you can learn from an open-source project with 250 million downloads - Dennis Doomen - NDC Oslo = 55:34
H676IkYOgdY = 2 weeks ago = Tales of Data Architecture Evolution - Josef Goldstein - NDC Oslo 2023 = 58:02
TuG0yKf8RSQ = 2 weeks ago = Flexible Authorisation with ASP.NET Core 7.0 - Jason Taylor - NDC Oslo 2023 = 35:44
GVU_JbLksdo = 2 weeks ago = The AI ethics session nobody knew we needed - Luise Freese and Iona Varga - NDC Oslo 2023 = 59:33
KGB5RJY6J6Q = 2 weeks ago = Micro Frontends & how we applied it in the Chase App - Teresa wu - NDC Oslo 2023 = 41:25
eQOM-UrNTS4 = 2 weeks ago = Balancing Coupling in Software Design - Vlad Khononov - NDC Oslo 2023 = 56:13
XFCUQKTwdIU = 2 weeks ago = Tactics for Building Background Services in .NET - Kevin Griffin - NDC Oslo 2023 = 1:00:03
NXjSJYyByzE = 2 weeks ago = Understanding Big Data for Software Engineers - David Ostrovsky - NDC Oslo 2023 = 58:29
xse3DOwPwZY = 2 weeks ago = Fixing your layout headaches - Erik André Jakobsen - NDC Oslo 2023 = 15:16
xvuPoN3cJXk = 2 weeks ago = Succeeding at Reactive Architecture - Ian Cooper - NDC Oslo 2023 = 59:22
BOFyC_ZK_RQ = 2 weeks ago = Can I crunch numbers on my GPU from .NET? - Yes you can, and it's easy! - Tor Kristen Haugen = 15:51
uhaaPgUQ_Ws = 2 weeks ago = Transformation Blueprint for Developer-Centric Application Security - Larry Maccherone - NDC Oslo = 1:04:23
bTl9wdbWS-o = 2 weeks ago = Video editing on the command line aka. what happens when you ask a programmer to edit your video = 16:04
044BdKO71zc = 2 weeks ago = Unleash the Power of Nuke: Consistent .NET Build Automation - Per Haagensen - NDC Oslo 2023 = 13:46
yQHoUDdoZe0 = 2 weeks ago = Have I Been Pwned: Serving billions of requests and terabytes of data without going broke! - Stefán = 37:10
tkEokNZEceE = 2 weeks ago = Infrastructure as Code on Azure: Bicep vs Terraform vs Pulumi - Erwin Staal - NDC Oslo 2023 = 53:28
qQYzJWj99Mo = 2 weeks ago = Ringbased Gated Releases - reliable and automated Deployments with Github Actions - Thomas Tomow = 54:28
IeTzCt9q75c = 2 weeks ago = Don't Panic: A Developer's Guide to Building Secure GraphQL APIs - Meenakshi Dhanani - NDC Oslo 2023 = 39:05
kose7u2WHBs = 2 weeks ago = How we revolutionized developer experience with 3.5 Platform Engineers - Jessica Andersson = 38:24
bJXPAhEzvXc = 2 weeks ago = Tight Genes: Intro to Genetic Algorithms - Dave Aronson - NDC Oslo 2023 = 45:46
M6XOniVANKI = 2 weeks ago = Understanding Probabilistic Data Structures with 112,092 UFO Sightings - Guy Royse - NDC Oslo 2023 = 54:50
O60aOTfaKrw = 2 weeks ago = Rebuilding Twitter Following Clean Architecture and Domain-Driven Design - Amichai Mantinband = 59:03
rL8ckLV_oRQ = 2 weeks ago = Real-time applications with Azure Web PubSub - Poornima Nayar - NDC Oslo 2023 = 52:46
k1EGiZUOFFg = 2 weeks ago = How to handle the luxury of having too much training data - Mathilde Ørstavik - NDC Oslo 2023 = 54:08
xI2xf2AvWno = 2 weeks ago = Powering the Front-end with React, GraphQL and Relay - Martin Artola - NDC Oslo 2023 = 59:54
NlBjVJPkT6M = 2 weeks ago = You are doing logging in .NET wrong. Let’s fix it. - Nick Chapsas - NDC Oslo 2023 = 49:28
qZVY9gYSe_c = 2 weeks ago = Crypto Heist: The Aftermath of a Government Website Cryptojacking Attack - Scott Helme - NDC Oslo = 46:17
V2S5odp-co4 = 2 weeks ago = Calculating the Value of Pie: Real-Time Survey Analysis With Apache Kafka® - Danica Fine - NDC Oslo = 1:00:03
pGgsFW7kDKI = 2 weeks ago = Performance tricks I learned from contributing to open source .NET packages - Daniel Marbach = 58:46
i9Q-hUwYmII = 2 weeks ago = Property-Based Testing - Lucy Mair - NDC Oslo 2023 = 47:24
jnDchr5eabI = 2 weeks ago = Practical Event Sourcing with Marten and .NET - Oskar Dudycz - NDC Oslo 2023 = 59:32
1MZpVcWIVW4 = 2 weeks ago = OAuth2 on a national level - how to secure extremely sensitive apis - Rune Andreas Grimstad = 59:26
IGl-P4SHo2E = 2 weeks ago = The top 5 JavaScript issues in all our codebases - Phil Nash - NDC Oslo 2023 = 46:45
llqLHqCseWg = 2 weeks ago = Abusing GitHub for fun and profit: Actions and Codespaces Security - Magno Logan and Nitesh Surana = 53:30
lW0gxMbyLEM = 2 weeks ago = What comes after Git? or, Building a cloud-native version control system in F# - Scott Arbeit = 1:00:03
XsuZQwK3m5c = 2 weeks ago = Are your secrets secure? How mobile applications are leaking millions of credentials - Mackenzie J. = 53:00
51ZUDsaxVKM = 2 weeks ago = The Next Decade of Software Is About Climate - What Is the Role of ML? - Sara Bergman = 56:58
MpzRe-BSEWs = 2 weeks ago = Updating Old .NET Framework Apps: Tips + Tricks to Help Make You More Prepared - Isaac Levin = 54:37
NsjVEMKhxmc = 3 weeks ago = CSS in 2023 and beyond - Anton Ball - NDC Oslo 2023 = 51:09
djyt_mG3S60 = 3 weeks ago = CDNs 101: An Introduction to Content Delivery Networks - Jake Ginnivan - NDC Oslo 2023 = 53:15
-USODEI-kgg = 3 weeks ago = Chasing the holy grail: reusable web components and design tokens - Duncan Hunter - NDC Oslo 2023 = 57:58
x_OKoJ_1j8U = 3 weeks ago = .NET gRPC - deep dive - Irina Scurtu - NDC Oslo 2023 = 59:24
qHmOm177tbQ = 3 weeks ago = Clone yourself with Azure Custom Neural Voice - Callum Whyte - NDC Oslo 2023 = 58:07
HmvXoW0r83I = 3 weeks ago = Demystifying OAuth, JWTs and Azure AD - Graeme Foster - NDC Oslo 2023 = 59:08
3vuu_SDnl-c = 3 weeks ago = It’s Your Decision. Where Do You Want to Take Your Career? - Leslie Martinich  - NDC Oslo 2023 = 47:02
npVfxDiEyeg = 3 weeks ago = Developing microservices like a boss with Dapr and Azure Container Apps - Jakob Ehn - NDC Oslo 2023 = 1:02:56
ttYQzHPe5s4 = 3 weeks ago = A Contrarian View of Software Architecture - Jeremy Miller - NDC Oslo 2023 = 51:18
dDANjr5MCew = 3 weeks ago = Common mistakes in EF Core - Jernej Kavka - NDC Oslo 2023 = 1:03:43
yBzV95MVgGg = 3 weeks ago = Copenhagen Developers Festival 2023 = 1:01
m4HIV5FLKms = 3 weeks ago = Copenhagen Developers Festival 2023 = 1:01
o9nVKE__nBo = 3 weeks ago = Warpforge: Decentralized supply chain management for building... Everything! - Eric Myhre = 55:09
gzSrzfrgFAA = 3 weeks ago = A Teacher, an Economist and a Developer Walk Into a Bar - Adele Carpenter - NDC Oslo 2023 = 47:37
VovctCSni-E = 3 weeks ago = Closing the documentation gap with Backstage.io - Martin Ehrnst & Bastiaan Wassenaar - NDC Oslo 2023 = 1:01:16
mrGfahzt-4Q = 3 weeks ago = Email vs Capitalism, or, Why We Can't Have Nice Things - Dylan Beattie - NDC Oslo 2023 = 56:46
A3TQ704THR0 = 3 weeks ago = My Worst Code Was My Best Code - Liam Westley - NDC Oslo 2023 = 55:58
QkbniViOGbc = 3 weeks ago = Building Distributed GraphQL APIs - Michael Staib - NDC Oslo 2023 = 1:04:46
4OmGiNh1kYE = 3 weeks ago = Accessibility - how to get the job done in a highly collaborative manner - Kjersti K. & Frank Dahle = 1:01:30
Eubk452UbXI = 3 weeks ago = Web Accessibility Deep Dive - Josefine Schaefer - NDC Oslo 2023 = 37:47
d41dUoiq6p8 = 3 weeks ago = Dev Containers. What are they and why do you need them? - Joseph Guadagno - NDC Oslo 2023 = 56:18
ld2v86xA6cY = 3 weeks ago = Demystifying web performance tooling and metrics - Anna Migas - NDC Oslo 2023 = 48:41
r3IKpPe36nY = 3 weeks ago = Azure Static Web Apps with Blazor and .NET - Melissa Houghton - NDC Oslo 2023 = 43:46
yV97QwC5gnE = 3 weeks ago = High Optionality Programming: Architectural Choices That Mitigate Technical Debt - Aaron Stannard = 1:00:19
n6kiJKr4_oA = 3 weeks ago = Back to Basics: Efficient Async and Await - Filip Ekberg - NDC Oslo 2023 = 1:01:25
ZYfdjszs8sU = 3 weeks ago = Stop using Entity Framework as a DTO provider! - Chris Klug - NDC Oslo 2023 = 46:46
Sz-wXOlsRKI = 3 weeks ago = The Chips and Pickle Story: What's Really Behind Infamous, Historic UI Failures? - Dean Schuster = 49:35
GQu749R8Sbo = 3 weeks ago = AKS Survival Pack: what to consider before going all-in with AKS - Kristina Devochko - NDC Oslo 2023 = 1:01:39
O5zDfmKiYLQ = 3 weeks ago = Using WordPress as a Modern Web Dev - Amy Kapernick - NDC Oslo 2023 = 56:18
_lYT-knNMTI = 3 weeks ago = The Principles of Green Software - How Green is Your Application - Sara Bergman - NDC Oslo 2023 = 10:55
c4AJlZeX2fE = 3 weeks ago = Practical OpenTelemetry for .NET - Martin Thwaites - NDC Oslo 2023 = 1:00:10
hYBa0XsqyuE = 3 weeks ago = Mixed Reality check - Scott Leaman - NDC Oslo 2023 = 10:16
HEiv03q8lcU = 3 weeks ago = Celebrity Deathmatch: Akka.NET vs Orleans - Hannes Lowette - NDC Oslo 2023 = 1:00:56
msNjvbKlWRE = 3 weeks ago = Efficient Learning for Developers  Tips and Strategies - Tav Herzlich  - NDC Oslo 2023 = 46:19
TgMBC6iSvsA = 3 weeks ago = A Performance Test on Steroids! - Jens Hordvik - NDC Oslo 2023 = 8:36
E50dAcu8KB8 = 3 weeks ago = Developing resilience for the future of work - Michelle Mannering - NDC Oslo 2023 = 1:01:47
KJxsro_V0kY = 3 weeks ago = Intentional Code - Minimalism in a World of Dogmatic Design - David Whitney  - NDC Oslo 2023 = 52:47
_iqcMdEOrF4 = 3 weeks ago = Monorepo – How to do frontend faster, better and safer - Kari Meling Johannessen - NDC Oslo 2023 = 1:03:20
5woZK_3z25U = 3 weeks ago = Deep Dive into Advanced TypeScript: A Live Coding Expedition - Christian Woerz - NDC Oslo 2023 = 47:39
PQIHeBSL4Rg = 4 weeks ago = Automating your DNS - Vatsalya Goel - NDC Oslo 2023 = 54:23
FLvY78ZFJMI = 4 weeks ago = 1,2,3… testing: is this thing on(line)? Meet your new Microsoft Testing tools - Mike Martin = 1:02:00
B4abZFFafs4 = 4 weeks ago = OAuth and Proof of Possession - The long way round - Dominick Baier - NDC Oslo 2023 = 47:16
4HEd1EEQLR0 = 4 weeks ago = C4 models as code - Simon Brown - NDC Oslo 2023 = 1:00:02
8aFbWny684Q = 4 weeks ago = Maximizing Efficiency and Minimizing Costs with Unreal Engine - Joakim Vindenes - NDC 2023 = 10:43
ttOImf17IGc = 1 month ago = Introduction to Smith-Waterman – An accurate DNA sequencing algorithm - Adam Gaidi - NDC Oslo 2023 = 11:10
lUQW8b2Jveo = 1 month ago = Automation of GUI testing using visual regression testing - Audun Wigum Arbo - NDC Oslo 2023 = 12:07
2LMEJ-WGFTk = 1 month ago = You Keep Using That Word: Asynchronous And Interprocess Comms - Sam Newman - NDC Oslo 2023 = 52:26
nkBL340zOaM = 1 month ago = Frontend Architectures: The Next Generations - Mikael Brevik - NDC Oslo 2023 = 47:02
feM64m6Csqw = 1 month ago = Building a dedicated platform for frontend developers @ NAV - Hans Kristian Flaatten Andreas Nordahl = 56:52
mMFfwTIejo0 = 1 month ago = Riding the wave of complexity - Markus Fanebust Dregi - NDC Oslo 2023 = 50:00
hf8hzGb2C6E = 1 month ago = Use your source code to document your application - Michaël Hompus - NDC London 2023 = 1:00:20
dZBADaF8R7k = 1 month ago = Azure Static Web Apps for the Enterprise - Stacy Cashmore - NDC London 2023 = 58:57
veCI1LZIFKM = 1 month ago = The Metaverse - Beyond the buzzword - Andreas Erben - NDC London 2023 = 59:29
BTgp9VyZSs8 = 1 month ago = Uno Platform: Your Apps Everywhere - Martin Zikmund - NDC London 2023 = 52:02
ml2JLU52tGo = 1 month ago = The Future of Cookies - Anders Abel - NDC Oslo 2023 = 52:55
-NdkAW_NAb8 = 1 month ago = Introduction to Actor-based Development with Project Orleans - Chris Klug - NDC Oslo 2023 = 59:10
pFwb4gqC5CQ = 1 month ago = Exciting new features in SQL Server for developers - Hasan Savran - NDC London 2023 = 55:36
Xl2Cetxg46A = 1 month ago = Maths or magic? End-to-end encryption explained like I'm five - Paolo Insogna - NDC London 2023 = 29:02
_7qeX88E3sc = 1 month ago = Making a difference in open-source - Florian Verdonck - NDC London 2023 = 50:36
f0QRTLKax3s = 1 month ago = OpenTelemetry tracing for .NET developers - Vagif Abilov - NDC London 2023 = 50:47
bZb7cyT5MA8 = 1 month ago = .NET 7 API diff - Stefan Pölz - NDC Oslo 2023 = 1:01:04
97edVjDT3kg = 1 month ago = How do I help my son? Revisited! - Dennie Declercq and Ivette Marchand - NDC Oslo 2023 = 56:01
haTnHdChzyY = 1 month ago = The invisible elephant in the room - Magali Milbergue - NDC London 2023 = 54:52
JT3CXCeHizs = 1 month ago = Testing in Production - Talia Nassi - NDC London 2023 = 34:25
2SpYbEfp4vA = 1 month ago = Understanding Probabilistic Data Structures with 112,092 UFO Sightings - Guy Royse - NDC London 2023 = 58:32
-LuYEdcMT-s = 1 month ago = How to steal Azure DevOps secrets - Björn Weström - NDC London 2023 = 39:01
z1gCR6vB8rU = 1 month ago = Ethical Machine Learning - Kesha Williams - NDC Oslo 2023 = 49:31
Nw4pgn484dI = 1 month ago = Secrets of building robust UI components - Glenn Reyes - NDC Oslo 2023 = 33:47
kAC6YWgSe7k = 1 month ago = 50 ways to show your data - Thomas Hütter - NDC London 2023 = 1:01:09
KpSSTaTl9Wc = 1 month ago = Is everything difficult or is it just me? - Jo Franchetti - NDC London 2023 = 1:03:52
8xSoeMJhe98 = 1 month ago = Property-Based Testing - Lucy Mair - NDC London 2023 = 50:51
aEA-iPHIt24 = 1 month ago = The Computer Science Behind Colour - Hayley Stewart - NDC London 2023 = 53:37
mXKGq9qC93Y = 1 month ago = Building a Realtime Websocket API in Phoenix - Jamie Wright - NDC Oslo 2023 = 45:51
FgGHquE_dYA = 1 month ago = Adventures in Rendering Off the Main Thread - Simon MacDonald - NDC Oslo 2023 = 46:57
AfTqoNiWCvQ = 1 month ago = Throw away your Xbox - The future of games is written in JavaScript - Opher Vishnia - NDC London = 53:49
iOp3mN933Og = 1 month ago = Let's Code an incremental source generator with Roslyn - Stefan Pölz - NDC London 2023 = 1:04:02
NBORkynL1RE = 1 month ago = Psychologically Safe Reliability Management - = 39:42
REKbn6Bc36M = 1 month ago = Azure Static Web Apps with Blazor and .NET - Melissa Houghton - NDC London 2023 = 48:10
FuR0-vjztio = 1 month ago = What's new in C#? - Exciting new features in C# 9, 10 and 11! - Filip Ekberg - NDC Oslo 2023 = 59:38
WEVC8j9AqNE = 1 month ago = Hacked on national television - Linus Kvarnhammar - NDC Oslo 2023 = 57:59
96rkexbc2Ag = 1 month ago = One Serverless Principle to Rule Them All: Idempotency - Adrienne Braganza Tacke - NDC London 2023 = 29:48
IlluGh16OKg = 1 month ago = VSCode for the C# Developer - Tim Corey - NDC London 2023 = 54:20
48cdGLIvYAM = 1 month ago = Tactics for Building Background Services in .NET - Kevin Griffin - NDC London 2023 = 1:00:14
vw2XffPmlYo = 1 month ago = Intentional Code - Minimalism in a World of Dogmatic Design - David Whitney - NDC London 2023 = 50:17
PyLE8ujGQMg = 1 month ago = Architecting Fortresses: A Deep Dive into Advanced Security Measures for ReactJS Apps - Jim Manico = 53:37
fO24yEXd028 = 1 month ago = AI for Inclusive Society - Responsible AI - Yashoda Singh - NDC Oslo 2023 = 1:02:22
UUs1nNIzGyY = 1 month ago = Fun with Algorithms - Tess Ferrandez-Norlander - NDC London 2023 = 56:42
2buWVsQ7stk = 1 month ago = Keynote: Why web tech is like this - Steve Sanderson - NDC London 2023 = 1:00:42
acGvHkl4uto = 1 month ago = OpenAPI & .NET: You're Doing It Wrong - Mark Rendle - NDC London 2023 = 1:01:08
lqQn9lnz2NU = 1 month ago = User testing in production: how to run a public beta - Eli Holderness - NDC London 2023 = 47:26
3JARMLD2gus = 1 month ago = Rules to better ChatGPT and using the best API ever ⭐ - Adam Cogan - NDC Oslo 2023 = 1:03:03
gO9MAZDIK5Y = 1 month ago = NDC TechTown 2023 = 1:09
lSRlfThoWKM = 1 month ago = Deploying your JS App Anywhere with .NET MAUI - Alyssa Nicoll - NDC London 2023 = 44:00
BvAsZKQyfTI = 1 month ago = NDC Oslo 2023 summed up by Michelle Mannering. Up Next Copenhagen Developers Festival. = 1:01
Ak8zNGblQMw = 1 month ago = COPENHAGEN DEVELOPER'S FESTIVAL = 1:01
Sxyt_V9fYqE = 1 month ago = Spaces, squares, and circles - an intro to UI design - Ash Banaszek - NDC London 2023 = 1:02:16
ahl6KeqQDlE = 1 month ago = Pilot Critical Decision Making skills - Clifford Agius - NDC London 2023 = 1:09:24
NMPeAW2RWdc = 1 month ago = Refactoring Is Not Just Clickbait - Kevlin Henney - NDC London 2023 = 1:07:25
Yo6N66lud50 = 1 month ago = From Domain Boundaries to Software Architecture - Maxime Sanglan-Charlier = 53:53
88_LUw1Wwe4 = 1 month ago = Top 5 techniques for building the worst microservice system ever - William Brander - NDC London 2023 = 40:44
oKLVzK_pqgg = 1 month ago = Discussing Backend For Front-end - Nicolas Fränkel - NDC London 2023 = 40:53
frbkYkXKuj8 = 1 month ago = Copenhagen Developers Festival 2023 = 1:01
pa1axIs2Dco = 1 month ago = Designing and Facilitating Better Workshops - Nick Tune, Mike Rozinsky & Dan Young - NDC London 2023 = 59:13
prLRI3VEVq4 = 1 month ago = Building Operable Software with TDD (but not the way you think) - Martin Thwaites - NDC London 2023 = 51:42
qs_mmezrOWs = 1 month ago = Building confidence in concurrent code with a model checker - Scott Wlaschin - NDC London 2023 = 1:07:15
CdcApjTBLEM = 1 month ago = Logging, tracing and metrics: instrumentation in .NET and Azure - Alex Thissen - NDC London 2023 = 1:00:56
3F3o6RbDfzs = 1 month ago = Build it fast, make it quick - Cory Gideon - NDC London 2023 = 52:03
nla1LGT83FE = 1 month ago = The Modern Trolley Problem - Responsible AI Principles - Michelle Sandford - NDC London 2023 = 58:21
VG9nomXfI4o = 1 month ago = Pride & Prejudice & C# - Simon Painter - NDC Oslo 2023 = 31:28
zCeGMsta5bY = 1 month ago = Building games in .NET MAUI - Shaun Lawrence - NDC London 2023 = 54:29
D0nn3aKEWx4 = 1 month ago = GitHub + Azure: Better Together! - April Edwards - NDC London 2023 = 54:41
4xpjlqIlfY8 = 1 month ago = Apache Kafka in 1 hour for C# Developers - Guilherme Ferreira - NDC London 2023 = 54:52
gWGP7R5fcBk = 1 month ago = Power BI for the Developer - Peter Myers & Chris Webb = 58:22
bZdYpYQb958 = 1 month ago = Running Blazor in production, lessons learned - Jimmy Engström - NDC London 2023 = 56:32
eM3HWYQcJVk = 1 month ago = Super Hero Layouts - Anton Ball - NDC London 2023 = 45:52
nTj6jazybgY = 1 month ago = Incident Management - Talk the Talk, Walk the Walk - Hila Fish - NDC London 2023 = 45:24
gGVBE0TPrFk = 1 month ago = It’s easy to create a good looking product, but what about a useful one? - Eleftheria Batsou = 32:25
Wn1Cj7785i8 = 2 months ago = Micro-Frontends in AWS - Luca Mezzalira - NDC London 2023 = 58:30
9cgzjjiU8Rg = 2 months ago = How to use Chrome DevTools to improve accessibility of your webpage - Dominika Zając = 46:47
WawXh_E6gqo = 2 months ago = Hostile JavaScript: Attacking and Defending the Browser - Todd Gardner - NDC London 2023 = 40:05
kqHYN1Y7pIc = 2 months ago = Introduction to Serverless with AWS Lambda in C# - Brandon Minnick - NDC London 2023 = 57:54
i38vNBGGcqo = 2 months ago = Defensive Coding Bootcamp - Heather Downing - NDC London 2023 = 42:01
zvqJmhJkPfE = 2 months ago = Message processing failed! But what's the root cause? - Laila Bougria - NDC London 2023 = 57:51
9ix0vVL34-M = 2 months ago = Where we're going... we don't need batch jobs - Adam Ralph - NDC London 2023 = 53:51
g3zmvdD8E38 = 2 months ago = Celebrity Deathmatch: Akka.NET vs Orleans - Hannes Lowette - NDC London 2023 = 1:01:06
GGUqyb6mzDw = 2 months ago = “Wouldn’t it be cool…” and other bad design approaches - Billy Hollis - NDC London 2023 = 1:04:30
Z82gsB-QIPs = 2 months ago = Lean and Lego: Building the Millennium Falcon - James Lewis - NDC London 2023 = 58:33
ys0DybCuhF0 = 2 months ago = What's new in C#? Exciting new features in C# 8.0, 9.0 and 10! -  Filip Ekberg - NDC London 2023 = 1:00:10
NFW5HUmw4sg = 2 months ago = Building cloud-ready applications in .NET - Layla Porter - NDC London 2023 = 1:02:16
oz9eXEKRL6w = 2 months ago = Ethical Machine Learning - Kesha Williams - NDC London 2023 = 54:10
6FOCNf06lqY = 2 months ago = You Keep Using That Word: Asynchronous And Interprocess Comms - Sam Newman - NDC London 2023 = 1:01:09
pYl_jnqlXu8 = 2 months ago = Goodbye controllers, hello Minimal APIs - Nick Chapsas - NDC London 2023 = 54:28
XiOpcIb1GGQ = 2 months ago = Hyper Speed! When Big Data Blooms - Scott Helme - NDC London 2023 = 47:54
iTBl7ZGzNvs = 2 months ago = Owning Your Experience: Talking about Mental Health In the Workplace - Arthur Doler = 53:33
RyYduqEi48A = 2 months ago = Interview with Ari Hunt - Adam Cogan - NDC Conferences = 10:49
dkd7yknbydA = 2 months ago = How to deprecate a feature the right way - William Bishop - NDC London 2023 = 36:35
3611y9h-U-0 = 2 months ago = Building Secure Microservices in Azure - Jimmy Bogard - NDC London 2023 = 1:04:36
7UBm8QFTaq0 = 2 months ago = Getting API security right - Philippe De Ryck - NDC London 2023 = 51:49
vkhtdgfHZYc = 2 months ago = Developing Flexible Authorisation Capabilities in ASP.NET Core - Jason Taylor - NDC London 2023 = 46:49
4WbOt5IKiUU = 2 months ago = How to Build a Quokkabot - Amy Kapernick - NDC London 2023 = 56:57
tOyXWtHwsWw = 2 months ago = Zero Downtime Application Deployments on Azure PaaS - Marcel de Vries - NDC London 2023 = 1:04:00
k0qTH6gx-1M = 2 months ago = CSS Techniques for Blazor Developers - Ed Charbeneau - NDC London 2023 = 1:02:44
oT0tSp83Qjg = 2 months ago = Emulating a Game Boy in .NET 6 - Wesley Cabus - NDC London 2023 = 56:05
kVAYsq9uv7I = 2 months ago = How Kubernetes optimisation can combat climate change - Annie Talvasto - NDC London 2023 = 59:29
NWBAS6YhAKc = 2 months ago = Running a real world, mission-critical system on Azure - Loek Duys - NDC London 2023 = 59:02
yUd798ly5-U = 2 months ago = Adding Live, Interactive Video to Your Application with Amazon IVS - Todd Sharp - NDC London 2023 = 51:14
QxBdzguISM4 = 2 months ago = An Infrastructure as Code Bake-off, comparing ARM, Terraform and Bicep - Mike Benkovich = 1:04:46
PaaORBYD3uc = 2 months ago = Exploring patterns to Debug Your Life - Dennie Declercq & Miriam Perrone - NDC London 2023 = 52:56
dhip9qSAiWo = 2 months ago = What is X++.net? - Brent Dawson - NDC London 2023 = 46:40
PbfeyIYjfH8 = 2 months ago = Exploring Serverless Options for .NET in Azure, AWS, and Beyond - Spencer Schneidenbach = 1:01:43
NxV19P7VKyI = 2 months ago = Sandboxing .NET assemblies for fun, profit and of course security! - Niels Tanis - NDC London 2023 = 56:25
Hl5EOslkpFk = 2 months ago = Practical tips to elevate your UX and accessibility - Jessica Engström - NDC London 2023 = 53:37
AlwmkatOUf4 = 2 months ago = .NET MAUI Blazor - Build Hybrid Mobile, Desktop, and Web apps - Gerald Versluis - NDC London 2023 = 1:02:06
qQScx1IckEc = 2 months ago = From App Security to Dev Security – Shift left with GitHub Advanced Security - Michael Kaufmann = 54:23
2AtNjxnwxZk = 2 months ago = Writing Code with Code: Getting Started with the Roslyn APIs - Steve Gordon - NDC London 2023 = 57:22
LCTZud6hwWM = 2 months ago = Functional Programming with C# - Simon Painter - NDC London 2023 = 1:09:05
fz389EfukQY = 2 months ago = A perfect match: Dapr & Azure Container Apps - Sander Molenkamp - NDC London 2023 = 1:02:06
LQ40Fc7K8tU = 2 months ago = Minimal APIs in ASP.NET 7.0 - Rob Richardson - NDC London 2023 = 1:05:35
oAJiQ1omuKY = 2 months ago = Vapourware: The best software that never was - Anders Norås - NDC London 2023 = 48:17
pKavkFkegGY = 2 months ago = Sockets, Sparks, and Magic Smoke - Dylan Beattie - NDC London 2023 = 58:33
O9XVr9Dz0xY = 2 months ago = The Future of Energy - Richard Campbell - NDC London 2023 = 1:00:55
0vQXhEqDvqs = 2 months ago = What's new in C# 11 - David Wengier - NDC London 2023 = 57:39
nXNYrbetzMM = 2 months ago = Clone yourself with Azure Custom Neural Voice - Callum Whyte - NDC London 202 = 1:06:27
Xsnbi00-oRc = 2 months ago = Keynote: Crypto means Cryptography! - Scott Helme - NDC Security 2023 = 58:01
p2GlRToY5HI = 2 months ago = Don’t Build a Distributed Monolith - Jonathan "J." Tower - NDC London 2023 = 1:04:02
YyWKczrfxW4 = 2 months ago = Succeeding at Reactive Architecture - Ian Cooper - NDC London 2023 = 59:11
2sTLr2q-JFc = 2 months ago = Building modern applications with GraphQL 2023 and beyond in ASP.NET Core 7 - Michael Staib = 1:05:03
corgQcXfTRw = 2 months ago = NOPASSWD: Building a Passwordless Cloud Infrastructure - Kyle Kotowick - NDC London 2023 = 49:47
ND_AjF_KTD8 = 2 months ago = The Next Decade of Software Development - Richard Campbell - NDC London 2023 = 1:07:05
iNHl2k9YJa4 = 2 months ago = Copenhagen Developers Festival 2023 = 1:01
hUnNfh8xJ1M = 2 months ago = Using WebAssembly to run, extend, and secure your .NET application - Niels Tanis - NDC Security 2023 = 52:36
fN4mojmju18 = 2 months ago = A data driven approach to application security - Petter Kvalvaag & Kristian Reed = 50:08
lVJpvXHq3r8 = 2 months ago = Google Family Link field test - Mateusz Krzeszowiec - NDC Security 2023 = 55:23
hc8n3pN0INA = 2 months ago = What the log4j incident taught us about Secure by Design - Daniel Deogun & Dan Bergh Johnsson = 58:08
hpFr8aioloU = 2 months ago = Block DNS exfiltration with dnsmasq proxy - Magnus Longva - NDC Security 2023 = 43:21
wi0x74iYiis = 2 months ago = Security as Code: A DevSecOps Approach - Joseph Katsioloudes - NDC Security 2023 = 51:36
7djRRjxaCKk = 2 months ago = What is Linux kernel keystore and why you should use it in your next application - Ignat Korchagin = 58:02
xSjmvnyVKEA = 2 months ago = How hacking works - Espen Sande-Larsen - NDC Security 2023 = 55:06
i0SizZk2Q-A = 2 months ago = How AI is impacting cybersecurity. Does it? - Victoria Almazova = 1:02:07
Bf2dUYkfYv0 = 2 months ago = Running system tests with active authn/z - Lars Skjorestad - NDC Security 2023 = 48:47
V-SgiA-D9r0 = 2 months ago = Test Driven Application Security - Tobias Ahnoff & Martin Altenstedt - NDC Security 2023 = 52:53
Qv7GErpqR-s = 2 months ago = What I learnt about automating security - George Coldham - NDC Security 2023 = 43:51
RT0PWBWp8wc = 2 months ago = Using seccomp to limit the Linux kernel attack service - Michael Kerrisk - NDC Security 2023 = 1:02:38
dtbBxa09Fxk = 2 months ago = What happens if I change this URI… oooooh - Halvor Sakshaug - NDC Security 2023 = 54:56
0D4mwpIxaQI = 2 months ago = Attacking through the Software Supply Chain - Felix Leder - NDC Security 2023 = 57:45
AOt_y6iZ2kI = 2 months ago = Building a sustainable security requirements process with the ASVS - Josh Grossman - NDC Security = 54:41
zlPBufBzscg = 2 months ago = In Defence of PHP - Stephen Rees-Carter - NDC Security 2023 = 59:47
1HrTpehfdPM = 2 months ago = Hacking the Juice Shop - Cecilia Wirén - NDC Security 2023 = 48:14
_zERV-BIV9Q = 2 months ago = Is this okay!? How to review code for security issues - Rouan Wilsenach - NDC Security 2023 = 54:33
a2x9pkIKhRc = 2 months ago = GitHub Actions: Vulnerabilities, Attacks, and Counter-measures - Magno Logan - NDC Security 2023 = 56:32
IjVnZAnKT0Q = 2 months ago = Defendable Products: How we try to improve security in our products - Ståle Pettersen - NDC Security = 1:00:45
bkU2fLN5nZE = 2 months ago = OPA everywhere! Exploring new opportunities in policy evaluation - Anders Eknert - NDC Security 2023 = 1:05:55
8tW1B9xip68 = 2 months ago = Lost and Found in Translation - Camilla Montonen = 54:17
tPdDS3UZpOQ = 3 months ago = Securely deploying Infrastructure as Code - Chris Ayers - NDC Security 2023 = 1:00:18
zbgxJRM_Y8U = 3 months ago = Cyber Security vs. Statistics - Christopher Van Der Made = 54:38
boEPpiqjb7Y = 3 months ago = Improving the Chances of Success in Secure Software Development - Daniela Cruzes & Espen A. Johansen = 59:42
gNuIwkBc92Q = 3 months ago = OAuth – the good Parts - Anders Abel - NDC Security 2023 = 59:40
rAtAfR88RnM = 3 months ago = Hyper Speed! When Big Data Blooms - Scott Helme - NDC Security 2023 = 54:32
nT355Ico1Bk = 3 months ago = NOPASSWD: Building a Passwordless Cloud Infrastructure - Kyle Kotowick - NDC Security 2023 = 40:25
aat-Uqa4Q-Y = 3 months ago = Introducing the OWASP Top 10 for Kubernetes - Steve Wade - NDC Security 2023 = 51:03
KBZAUi9OPww = 3 months ago = Return Oriented Programming, an introduction - Patricia Aas - NDC Security 2023 = 56:57
9Z3r_qvU_Tk = 3 months ago = So long secure coding... Hello secure development! - Laura Bell - NDC Sydney 2022 = 1:01:57
cyRNeUFOJjU = 3 months ago = Turbo Eureka - Mike Long & Øyvind Fanebust - NDC Security 2023 = 50:19
33MJQyLhhxs = 3 months ago = RBAC to the Future: Untangling Authorization in Kubernetes - Jimmy Mesta - NDC Security 2023 = 35:11
BkigVNNSurI = 3 months ago = OAuth and the long way to Proof of Possession - Dominick Baier & Steinar Noem - NDC Security 2023 = 58:15
hWJuX-8Ur2k = 3 months ago = Securing SPAs and Blazor Applications using the BFF (Backend for Frontend) Pattern - Dominick Baier = 1:03:16
OpFN6gmct8c = 3 months ago = The insecurity of OAuth 2.0 in frontends - Philippe de Ryck - NDC Security 2023 = 57:18
u6hiW-LPpso = 5 months ago = A comprehensive, pragmatic, ethical exploration of Web3 - Rob Moore - NDC Sydney 2022 = 1:00:34
onpBW9b8bMs = 5 months ago = A mortal's guide to making a pig run faster - Richard Banks - NDC Sydney 2022 = 58:56
ngOu9HL9sS8 = 5 months ago = Coding in the Cloud with GitHub Codespaces - Faten Healy - NDC Sydney 2022 = 50:57
mFiAhYaKao4 = 5 months ago = Securing your .NET application software supply-chain - Niels Tanis - NDC Sydney 2022 = 57:55
XeC2vLp1BV4 = 5 months ago = You Shall Not Password: Modern Authentication for Web Apps - Eli Holderness - NDC Sydney 2022 = 50:30
QK0xRG4Be6k = 5 months ago = No, I don't need servers for .NET development in AWS! - Rob Van Pamel - NDC Sydney 2022 = 59:46
BPTCGq6TgBE = 5 months ago = Mayday! Software lessons from aviation disasters - Adele Carpenter - NDC Sydney 2022 = 52:43
cyCaXwbW7h8 = 6 months ago = Effective DevOps for Organizations - Anthony Borton - NDC Sydney 2022 = 1:01:32
OG2hA4_hEKM = 6 months ago = Bicep - Deploy to Azure cloud without it being a pain in the ARM - Paul Glavich - NDC Sydney 2022 = 58:44
ILH1tJp0Vac = 6 months ago = Developing and Deploying Containers and Microservices with Azure Container Apps - Will Velida = 58:19
Q4qZPP9kphk = 6 months ago = How Kubernetes optimisation can combat climate change - Annie Talvasto - NDC Sydney 2022 = 46:56
OPr7kXxwUV4 = 6 months ago = Wearable Live Captions - Jo Franchetti - NDC Sydney 2022 = 38:15
63FLcPHUCPM = 6 months ago = Getting started with Kubernetes for your .NET Application - Martin Ullrich - NDC Sydney 2022 = 1:01:18
aSMCYbOxgkc = 6 months ago = Advanced TypeScript Type Utilities - Basarat Ali Syed - NDC Sydney 2022 = 1:00:49
tVmABHwxuqE = 6 months ago = How does Hot Reload even work? - David Wengier - NDC Sydney 2022 = 1:02:18
giw6wobivaI = 6 months ago = Microsoft DevOps on AWS - Mohamed Wali - NDC Sydney 2022 = 53:08
kMI1wAQ3XeQ = 6 months ago = Wish you were here: stories of building a remote development IDE - Matt Ellis - NDC Sydney 2022 = 1:01:09
VOEVE8j-Gfo = 6 months ago = What's new in C#? Exciting new features in C# 8.0, 9.0 and 10! - Filip Ekberg - NDC Sydney 2022 = 58:50
fsYahHAs0Sg = 6 months ago = 10 Tips to Rocking as an Azure Architect - Adam Cogan - NDC Sydney 2022 = 1:00:57
6haKMxdWeZY = 6 months ago = Message Brokering and Event Driven Architecture on Azure - Marilag Dimatulac Svennevig - NDC Sydney = 1:00:31
1koXN4s_vbw = 6 months ago = The Next Decade of Software Development - Richard Campbell - NDC Sydney 2022 = 1:04:20
U2McB8oo0Io = 6 months ago = Locknote: Programming’s Greatest Mistakes - Mark Rendle - NDC Oslo 2022 = 1:04:12
e3xl5kLiyJM = 6 months ago = How do our ideas about coding affect the software we create? - Christin Gorman - NDC Oslo 2022 = 34:01
gWlLRRzPEcA = 6 months ago = How I work with JSON - Einar Høst - NDC Oslo 2022 = 59:24
rDfH53TMFzU = 6 months ago = .NET and Microsoft’s Pivot to the Cloud - Richard Campbell - NDC Oslo 2022 = 51:07
wioBVpQnxGg = 6 months ago = Popcorn & Clocks; A story about scheduling in the browser - Stian Veum Møllersen - NDC Oslo 2022 = 48:20
mRbTMlE5ElA = 6 months ago = Fractal Architecture - Mark Seemann - NDC Oslo 2022 = 59:41
iIMQxjvs4zw = 6 months ago = Introduction to project Orleans for your distributed applications - Johnny Hooyberghs - NDC Oslo = 59:27
reZ9OhL7RKA = 6 months ago = Learning in public - Live coding on Twitch - Layla Porter - NDC Oslo 2022 = 1:00:33
gaoZdtQSOTo = 6 months ago = Let's build event store in one hour! - Oskar Dudycz - NDC Oslo 2022 = 57:47
bpEvbT8mkek = 6 months ago = Hyper Speed! When Big Data Blooms - Scott Helme - NDC Oslo 2022 = 49:16
QKsbzJFHaP0 = 6 months ago = Making Every Game and App More Accessible with .NET and AI - Alex Dunn - NDC Oslo 2022 = 55:18
QqvYIIobZ6A = 6 months ago = Learning to Love DDD - a Tale of Two Products - Chris Simon - NDC Oslo 2022 = 45:12
8NBbJe2odak = 6 months ago = Reactive Infrastructure - Piers Karsenbarg - NDC Oslo 2022 = 40:47
FR5kUgtmqg4 = 6 months ago = Standing on the Shoulders of Giants - Jiaranai Keatnuxsuo - NDC Oslo 2022 = 56:38
2QHGT1VW7Yk = 6 months ago = Monitoring and alerting like a pro with Azure Monitor/Application Insights - Stefán Sigurðarson = 51:56
yli4RwVgZrU = 6 months ago = Green Code 2020 - Anders Norås - NDC Oslo 2022 = 11:11
pkUoZF2vQvU = 6 months ago = Hidden features in MS Paint - Marianne Melhoos - NDC Oslo 2022 = 12:08
qnlJoz8heio = 6 months ago = Saving elephants with Raspberry Pi’s & Machine Learning - Thijs Suijten - NDC Oslo 2022 = 46:22
s6KZlL3Yt8s = 6 months ago = From nothing to state of the art - Alexander Vassbotn Røyne-Helgesen - NDC Oslo 2022 = 57:55
qsakF8zFJjA = 6 months ago = Sami stopwords - How far have we gotten and why does it matter? - Espen Klem - NDC Oslo 2022 = 13:42
N3Lou2V1iec = 6 months ago = Preparing for Disaster: Handling the Election and MGP at NRK.no - Ingrid Guren & John Arne Pedersen = 46:27
RdLV5yjDB0M = 6 months ago = 5 mistakes we made transforming to Platform teams in FINN.no - Vilde Opsal - NDC Oslo 2022 = 58:20
L_n-12FglLI = 6 months ago = How to create maintainable and testable Blazor components - Egil Hansen - NDC Oslo 2022 = 53:31
c6fSbjXxWgI = 6 months ago = Down the Oregon Trail with Functional C# - Simon Painter - NDC Oslo 2022 = 1:02:17
8BuCzpfp8Pk = 6 months ago = The Grand Unified Theory of Clean Architecture and Test Pyramid - Guilherme Ferreira - NDC Oslo 2022 = 47:27
KtKGbhksqsM = 6 months ago = A web for anyone, anywhere, anytime - Rowdy Rabouw - NDC Oslo 2022 = 1:01:03
8APa6lkdAAk = 6 months ago = 6 years of serverless – Lessons learned from real-world applications - Moukarram Kabbash - NDC Oslo = 56:08
8L7hb1eO9iU = 6 months ago = A bouquet of good and bad advice for young talents - Elin Brusberg - NDC Oslo 2022 = 11:30
53wocQ8KRkM = 6 months ago = Building a level 5 autonomous vehicle (in TrackMania) - Manu Gopinathan & Malte Loller-Andersen = 52:28
1YDBJNH2auc = 6 months ago = Super Hero Layouts - Anton Ball - NDC Oslo 2022 = 47:00
cGcrReJ6FbY = 6 months ago = Strangling The Monolith: Applied Patterns & Practices From The Trenches - Thomas Ploch = 1:01:25
iAO7HZZ1tMM = 6 months ago = Wearable Live Captions - Jo Franchetti - NDC Oslo 2022 = 37:06
Z9DJzVJD_vg = 6 months ago = Forget about OAuth 2.0. Here comes OAuth 2.1 - Philippe De Ryck - NDC Oslo 2022 = 54:27
vrRXIQDCCEk = 6 months ago = Writing a compiler with LLVM - Cailin Smith - NDC Oslo 2022 = 47:58
UdQJWcgOnJg = 6 months ago = Building Secure Microservices in Azure - Jimmy Bogard - NDC Oslo 2022 = 1:02:40
gcETqDQkw5E = 6 months ago = Visualization for Effective Testing and Learning - Davrondzhon Gafurov - NDC Oslo 2022 = 49:29
cSVvhUnE4hc = 6 months ago = What I Learnt Fixing 50+ Broken Kubernetes Clusters - David Flanagan - NDC Oslo 2022 = 45:18
KPsG8xo5ouI = 6 months ago = Remixing Frontend Development - Kristofer Selbekk - NDC Oslo 2022 = 58:46
BO6qHQbKFsw = 6 months ago = Testing at scale - Adam Furmanek - NDC Oslo 2022 = 56:23
OVN-yLFbNs8 = 6 months ago = Help! I've created a serverless monolith! - Marc Duiker - NDC Oslo 2022 = 41:50
DktkFTTFLHE = 6 months ago = WhatsApp, Web3, and Wordle: Evolving a Digital Society - Dylan Beattie - NDC Oslo 2022 = 1:14:19
-THd1Su3vxE = 6 months ago = Effective DevOps for Organizations - Damian Brady - NDC Oslo 2022 = 54:07
SjOMLj3NE-4 = 6 months ago = Don't Panic - how to get back into your learning zone! - Maarten Hoppen - NDC Oslo 2022 = 57:07
hhsYomkjC8E = 6 months ago = Building beautiful Blazor apps with Tailwind CSS - Chris Sainty - NDC Oslo 2022 = 58:45
bH4VD1KqUQI = 6 months ago = Securing SPAs and Blazor Applications using the BFF (Backend for Frontend) Pattern - Anders Abel = 1:01:38
iZy4c3m0M3M = 6 months ago = How To Not Strangle Your Coworkers: Resolving Conflict with Collaboration - Arthur Doler - NDC Oslo = 58:49
uOIi0K_mpUo = 6 months ago = Building that glorious monolith. And carving it too. - Glenn F. Henriksen - -NDC Oslo 2022 = 58:04
piUesxuZkIQ = 6 months ago = Refactoring Is Not Just Clickbait - Kevlin Henney - NDC Oslo 2022 = 1:03:44
yan1YOXvAUM = 6 months ago = Domain modelling in object-oriented and functional programming, based on C# and F# - Marcin Kern = 36:35
Zx5VIme3qJE = 6 months ago = Building a .NET Rocks! Podcast App in MAUI Blazor - Carl Franklin - NDC Oslo 2022 = 55:51
h4HP2osT6k4 = 6 months ago = Failure is Always an Option - Dylan Beattie - NDC Oslo 2022 = 51:46
Vt5Z9_3hf1U = 6 months ago = .NET MAUI What/How and Why - Clifford Agius - NDC Oslo 2022 = 1:02:20
8q050zzV8oo = 6 months ago = I'm just trying to keep my head above water - Chris Klug - NDC Oslo 2022 = 1:04:22
FlQOqUeoUD0 = 6 months ago = What's new in C#? Exciting new features in C# 8.0, 9.0 and 10! - Filip Ekberg - NDC Oslo 2022 = 1:00:15
amSuoBKG1Ns = 6 months ago = Writing a full-text search engine in TypeScript - Michele Riva - NDC Oslo 2022 = 53:15
1_4v1pHCoYc = 6 months ago = Vapourware: The best software that never was - Anders Norås - NDC Oslo 2022 = 38:45
dpRDGjyk2bg = 6 months ago = CSS in motion: Animations for fun and profit - Martine Dowden - NDC Oslo 2022 = 37:52
jGLZRQGGn54 = 6 months ago = Victory instinct and mental strength - Genette Våge - NDC Oslo 2022 = 45:53
deny3mBfccQ = 6 months ago = From F# to Python with Fable - Dag Brattli - NDC Oslo 2022 = 1:01:22
ZOyzP44HRHg = 6 months ago = We need to talk about Whistleblowing - Marion Løken - NDC Oslo 2022 = 59:17
MgYwvMrEO_I = 6 months ago = Parens of the Dead: Live pair programming and zombies - Magnar Sveen & Christian Johansen = 58:02
DZedEsu0OXc = 6 months ago = The Culture Map - Diego Garcia Lozano - NDC Oslo 2022 = 54:09
CYvYsSWzhpw = 6 months ago = How we secure NAV.no and 1/3 of Norway's national budget - Hans Kristian Flaatten - NDC Oslo 2022 = 53:23
CYKdNphIr-k = 6 months ago = .NET Rocks Live: Making OpenSource Work for Everyone - Carl Franklin/ Richard Campbell/David Whitney = 52:50
BSSCX4xUyT8 = 6 months ago = Amazing Algorithms for Solving Problems in Software - Barry Stahl - NDC Oslo 2022 = 54:23
B-a9ng9MGPo = 6 months ago = What happens if I change this URI… oooooh - Halvor Sakshaug - NDC Oslo 2022 = 49:07
-7vWIG1J0Tk = 6 months ago = An Underwater Dance with Data Engineering in Azure - Ashley Russell - NDC Oslo 2022 = 52:28
_IKP8dSiVkk = 6 months ago = Implementation of right-to-left languages on the frontend - Iryna Zelenetska - NDC Oslo 2022 = 16:15
Uv-qNbUStSM = 6 months ago = Secretless access to Azure SQL server using Managed Identity - Hallstein Brøtan - NDC Oslo 2022 = 12:59
UgzMj8mO9KA = 6 months ago = Practical Pipelines: A Houseplant Soil Alerting System with ksqlDB - Danica Fine - NDC Oslo 2022 = 1:05:26
ChuS0jXNS84 = 6 months ago = We must talk about String - Einar Høst - NDC Oslo 2022 = 14:08
9EI_lqPUVEE = 6 months ago = Garbage data in, garbage models out - Jodie Burchell - NDC Oslo 2022 = 45:51
-JfZDnRjz1k = 6 months ago = Smarter Everything with ML & the IoT - Brandon Satrom - NDC Oslo 2022 = 54:12
u_xn5BdJDGI = 6 months ago = Formal verification of C# smart contracts - Allister Beharry - NDC Oslo 2022 = 45:48
0NzmUgkbpwo = 7 months ago = Social Anxiety 2.0 - Dennie Declercq & Stacy Cashmore - NDC Oslo 2022 = 5:01:54
8SyCPmB6LA8 = 7 months ago = How to Build a Quokkabot - Amy Kapernick - NDC Oslo 2022 = 58:43
eClCqGs02Qk = 7 months ago = Help! We’re inheriting a large F# application - Matias Pettersen & Teodor Ande Elstad - NDC Oslo = 53:41
IUN3m3K-6nY = 7 months ago = Best-practices for securing your Azure Container Services - Sjoukje Zaal - NDC Oslo 2022 = 47:11
FKBh2SaQXUE = 7 months ago = Dungeons, Dragons, and Graph Databases - Guy Royse - NDC Oslo 2022 = 1:01:23
EgKg0QvvlDk = 7 months ago = Death to Latency: Building Reactive, Cloud Native Apps with Akka.NET - Aaron Stannard - NDC Oslo = 58:08
07ceY-VKsvw = 7 months ago = Web3 is a pyramid of dumpster fires - Odin Standal - NDC Oslo 2022 = 47:28
L8-_rtdHn08 = 7 months ago = Lean & Lego: Building the Millennium Falcon Redux - James Lewis - NDC Oslo 2022 = 56:00
-X-Q1pLcR2c = 7 months ago = How I designed the most efficient deepfake detector in the world with $100 - Mathis Hammel = 46:39
woevAXKb6U4 = 7 months ago = Embracing gRPC in .NET - Irina Scurtu - NDC Oslo 2022 = 59:49
QozjqbNhTVQ = 7 months ago = Fun with Algorithms - Tess Ferrandez-Norlander - NDC Oslo 2022 = 51:24
8XbuJ_DczL8 = 7 months ago = Effective testing in microservice systems - Christian Horsdal - NDC Oslo 2022 = 59:53
dwtVgOvGcQg = 7 months ago = Domain-Driven Design & Team Topologies For Product-led Organizations - Nick Tune - NDC Oslo 2022 = 49:24
sfrEc2UGWTY = 7 months ago = Observable Web Applications - Todd Gardner - NDC Oslo 2022 = 58:38
KfezmwfTu7Y = 7 months ago = The Problems Micro Frontends Won't Solve That No One Wants to Talk About - Jennifer Wadella = 45:18
_zjv0CHf--4 = 7 months ago = Exploring Source Generators - Martin Ullrich - NDC Oslo 2022 = 53:32
Wy-BmhB6ty4 = 7 months ago = Dealing with eventual consistency - Dennis van der Stelt - NDC Oslo 2022 = 51:00
c2AmXSoZAQ8 = 7 months ago = Turning Dreaming into Doing - A Life Manual for Nerds - Lars Klint - NDC Oslo 2022 = 1:00:10
ETLt8I57YyM = 7 months ago = Applied Functional Programming in Computational Genomics - Jamie Dixon - NDC Oslo 2022 = 52:33
3Qy3ReRcGes = 7 months ago = Change wings on the fly - Tatiana Kolesnikova - NDC Oslo 2022 = 44:33
9_UotaUwARU = 7 months ago = OAuth – the good Parts - Anders Abel - NDC Oslo 2022 = 57:06
Okdjn7o4q8E = 7 months ago = Count-min Sketch to Infinity - Steve Lorello - NDC Oslo 2022 = 1:00:16
grZdypDLibs = 7 months ago = Consuming GraphQL using C# - Brandon Minnick - NDC Oslo 2022 = 50:06
_9ULo-F4nmE = 7 months ago = At Least Once - Ian Cooper - NDC Oslo 2022 = 1:01:36
TPSxnrkaFGo = 7 months ago = The Future of Energy - Richard Campbell - NDC Oslo 2022 = 55:33
15k1HEBHYXc = 7 months ago = GitHub Copilot, using AI to help you learn, code, and build - Michelle Mannering - NDC Oslo 2022 = 59:35
mx3laBpmH8k = 7 months ago = The Curious Incident in your Software in the Day-Time - Liam Westley - NDC Oslo 2022 = 57:07
dEgjYMrt38A = 7 months ago = Defensive Coding Bootcamp -  - Heather Downing - NDC Oslo 2022 = 45:05
vNouCMGP1eE = 7 months ago = Advanced API and Integration Problems & Patterns - Udi Dahan - NDC Oslo 2022 = 1:02:09
D393nI_KM8s = 7 months ago = Why you shouldn't trust me - Keerthana Ganesh & Shubham Patil - NDC Oslo 2022 = 50:53
vQEYH4HhQog = 7 months ago = The Modern Trolley Problem - Responsible AI Principals - Michelle Sandford - NDC Oslo 2022 = 1:02:23
GSUUHTOGYjA = 7 months ago = Shrink The Web: How To Get Happier By Removing Crap - Lemon 🍋 - NDC Oslo 2022 = 1:00:51
xi-zv3dRWfk = 7 months ago = Share Pie: The DDD Treasure Hidden in Plain Sight - Nick Tune - NDC Oslo 2022 = 45:12
0xSmlVBhEFs = 7 months ago = Secret Management: The Soft Way - Lian Li - NDC Oslo 2022 = 1:01:49
DmpIhFNjv-0 = 7 months ago = How our critical systems fail, and what we do about it - Simon Randby & Fredrik Bekkevold - NDC Oslo = 53:06
zTbF919UAZk = 7 months ago = The Metaverse and the location problem - Scott Leaman - NDC Oslo 2022 = 56:44
_D1qLdhuuAU = 7 months ago = Take control of your cloud environment using IaC with Pulumi - Tomas Jansson - NDC Oslo 2022 = 58:26
1zaJ7PiSfW4 = 7 months ago = Serverless GraphQL in .NET with Azure Functions and Hot Chocolate - Michael Staib - NDC Oslo 2022 = 1:01:55
SXdNqRwEwDU = 7 months ago = Reducing the environmental footprint in nautical transport with F# & Serverless - Roman Provazník = 57:07
QGvzQSKprzM = 7 months ago = Look ma, no hands! - How to program without using your hands - Peder Voldnes Langdal - NDC Oslo = 13:42
bITu4GncVQc = 7 months ago = How to Manage your Ducks: Being a More Sustainable You - Amy Kapernick = 15:15
ZToDbkFyAto = 7 months ago = Death to Test Environments - Nikolai Norman Andersen - NDC Oslo 2022 = 11:20
yVQMnQKSsh4 = 7 months ago = Building Operable Software with TDD (but not the way you think) - Martin Thwaites = 51:54
CeSo8oax4f4 = 7 months ago = Betting the company on Clojure - Erik Assum = 17:00
o4mVlUY-TvI = 7 months ago = “Wouldn’t it be cool…” and other bad design approaches - Billy Hollis - NDC Oslo 2022 = 1:00:32
bC4ZNsc97Xk = 7 months ago = Web performance APIs you (probably) didn't know existed - Matheus Albuquerque - NDC Oslo 2022 = 59:07
kbTohfkZAMA = 7 months ago = Testing Web Applications with Playwright - Debbie O'Brien - NDC Oslo 2022 = 50:49
myR2MfcBvr0 = 7 months ago = I ♥️ Form Controls! - David Benson - NDC Oslo 2022 = 42:04
13nAqyGI7lw = 7 months ago = Down-to-Earth Cloud Scaling - Meg Gotshall - NDC Oslo 2022 = 45:49
LEMVBxkJ-9g = 7 months ago = Death by downtime - Dag Helge Østerhagen & Rune Andreas Grimstad - NDC Oslo 2022 = 57:19
p0oTrCZ5acE = 7 months ago = Keynote: Managing the Burnout Burndown - Anjuan Simmons - NDC Oslo 2022 = 54:34
rfIX0FzKHF0 = 7 months ago = Keynote: Abstraction Patterns - Kate Gregory - NDC TechTown 2022 = 1:02:42
cPbikKfDBNg = 7 months ago = Thinking Erlang in a connected world - Ali Sabil - NDC TechTown 2022 = 1:03:17
b4gJtXfrNfU = 7 months ago = Package management in C++ - Mikhail Svetkin - NDC TechTown 2022 = 1:00:37
MLmdy1ZMM9Y = 7 months ago = C++: what comes next? - Chandler Carruth - NDC TechTown 2022 = 57:58
IMkOCp0Q3zM = 7 months ago = Surviving a chip shortage - Inge Fredriksen - NDC TechTown 2022 = 59:17
W4cnO36kihs = 7 months ago = C++ Lambda Idioms - Timur Doumler - NDC TechTown 2022 = 56:29
HdZTw5qLg6A = 7 months ago = How C++23 changes the way we write code - Timur Doumler - NDC TechTown 2022 = 59:25
WHe-8Nzx9Ag = 7 months ago = A lock-free atomic shared_ptr - Timur Doumler - NDC TechTown 2022 = 1:03:22
BdKyq56Cijo = 7 months ago = Fundamentals of Embedded Linux - Chris Simmons - NDC TechTown 2022 = 1:04:15
8M8U1EgnUVw = 7 months ago = Getting started with Yocto Project - Chris Simmons - NDC TechTown 2022 = 1:03:27
e_zJYwB6eB0 = 7 months ago = 5 Years Of Teaching C++: A Retrospective - Martin Hořeňovský - NDC TechTown 2022 = 57:01
Gnyc75TRF1o = 7 months ago = Neotron - why write a brand new ‘DOS’ for Arm in Rust? - Jonathan Pallant - NDC TechTown 2022 = 1:00:34
DL9LANLg5EA = 7 months ago = Learning Rust the wrong way - Ólafur Waage - NDC TechTown 2022 = 51:54
lHCisBcw3kA = 7 months ago = Contemporary C++ in action - Daniela Engert - NDC TechTown2022 = 1:02:50
kmQQtoQ-Moc = 7 months ago = An Introduction To Floating Point Math - Martin Hořeňovský - NDC TechTown 2022 = 45:24
AriG-Wo3BYQ = 7 months ago = Identifying Common Code Smells (In C++) - Arne Mertz - NDC TechTown 2022 = 55:03
Ls8PLTO3Qas = 7 months ago = Lightning Updates - Hana Dusíková - NDC TechTown 2022 = 56:27
MNIqT6msRZY = 7 months ago = Making sense of Volatile - Inge Fredriksen - NDC TechTown 2022 = 41:41
qIblgUnkR0M = 7 months ago = 42 Silly Ways to say Hello in C - Olve Maudal - NDC TechTown 2022 = 58:10
cADdwFk2-7U = 7 months ago = Keynote: Lies Developers Tell Themselves - Billy Hollis - NDC Minnesota = 1:02:48
5igL_-Je83g = 7 months ago = Zephyr RTOS: Software power tools for constrained devices - Balaji Srinivasan & Eirik Midttun = 1:02:57
Fa8qcOd18Hc = 7 months ago = Signed Integers Considered Harmful - Robert Seacord - NDC TechTown 2022 = 1:00:59
RwSaDVubdKk = 7 months ago = MISRA C++202x: It ain't your grandpa's MISRA any more - Loïc Joly - NDC TechTown 2022 = 56:41
qnHpjgYekZs = 7 months ago = The Floor is Lava, trying to teach C++ - Patricia Aas - NDC TechTown 2022 = 54:32
5ZZUPk8wKWY = 7 months ago = Properties of Unit Tests - Arne Mertz - NDC TechTown 2022 = 1:06:44
zJIqq1XsPsg = 7 months ago = Auto-testing for situational awareness - James Westfall - NDC TechTown 2022 = 55:02
Icg248MNt2Q = 7 months ago = Code Analysis ++ - Anastasia Kazakova - NDC TechTown 2022 = 51:18
OGPmZzhDPYw = 7 months ago = How to start a program - Anders Schau Knatten - NDC TechTown 2022 2 = 1:00:54
8PD6vRBgQrg = 7 months ago = Analysis of Real World Apps with Frida - Kyle Ossinger - NDC TechTown 2022 = 51:29
ailViuK1gmk = 7 months ago = C++20 - My Favourite Code Examples - Nicolai Josuttis - NDC TechTown 2022 = 58:51
opRbU6WZH9s = 7 months ago = The Boeing 737 MAX: When Humans and Technology Don't Mix - Kyle Kotowick - NDC TechTown 2022 = 1:00:46
gvov-0CVYZc = 7 months ago = Breaking Dependencies: Type Erasure - The Implementation Details - Klaus Iglberger = 54:34
4H8IZyVEHaE = 7 months ago = Error handling in C++: as easy as "use exceptions"? - Vitaly Fanaskov - NDC Techtown 2022 = 44:02
7iyB4nHfUwQ = 8 months ago = Keynote: Securing the Future - Laura Bell - NDC Minnesota 2022 = 47:14
twMM9NQXRaI = 8 months ago = Keynote: The Next Decade of Software Development - Richard Campbell - NDC Minnesota = 1:03:10
-6iRgh9FCOs = 8 months ago = Keynote: Capability, Vulnerability, Fallibility, and Flexibility - Anjuan Simmons - NDC Minnesota 22 = 40:17
r8c6ws9Tow0 = 8 months ago = A Preview of C++ 23 - Daniela Engert - NDC TechTown 2022 = 1:04:05
VDiRdzdwgNc = 8 months ago = Theory makes beautiful programs - Jørgen Kvalsvik - NDC TechTown 2022 = 58:50
PmVmaT1JNbw = 8 months ago = Typical C++, But Why? - Björn Fahller - NDC TechTown 2022 = 53:54
UHvgzDzqutM = 8 months ago = NDC LONDON 2023 - The Agenda is Oot! = 0:46
W2D8Qjx5jQc = 8 months ago = #WinUIEverywhere - Nick Randolph - NDC Melbourne 2022 = 48:14
R1fCs2a2xXw = 8 months ago = JWT! What is it good for? Absolutely everything! - Ben Dechrai - NDC Melbourne 2022 = 19:07
NehPwM9eG7g = 8 months ago = Does Spam have an opinion? - Lars Klint - NDC Melbourne 2022 = 41:33
FXd31Lv34NA = 8 months ago = Apollo Federation: Connecting GraphQL Microservices - Allen Azemia - NDC Melbourne 2022 = 47:57
P-cC09vVG7M = 8 months ago = Developing Spidey Senses - Ron Dagdag - NDC Melbourne 2022 = 38:45
gE4Bo5ZjfgY = 8 months ago = Five Design Patterns to build resilient Applications - Derek Bingham - NDC Melbourne 2022 = 1:31:24
l9vMNGomm9s = 8 months ago = JavaScript apps go Int(ernationa)l - Phil Nash - NDC Melbourne 2022 = 42:53
tRfa93xp0SI = 8 months ago = Easier Deployments using a Green:Blue Strategy - Patrick Zhao - NDC Melbourne 2022 = 59:30
vNz7U8r5wjc = 8 months ago = Stop Caring about Kubernetes with Azure Container Apps & Dapr - Todd Whitehead - NDC Melbourne 2022 = 54:39
BfR08xNTL4w = 8 months ago = Building a Raspberry Pi Robot Arm with  NET 6, Blazor and SignalR - Peter Gallagher = 49:05
DyPzEfeHz64 = 8 months ago = Azure Kubernetes Services 101 for Developers - Jorge Arteiro - NDC Melbourne 2022 = 56:12
ZR8MHFTEtlc = 8 months ago = Mobile App Accessibility - Allison Ravenhall - NDC Melbourne 2022 = 32:45
STCaelGWEeA = 8 months ago = Down the Oregon Trail with Functional C# - Simon Painter - NDC Melbourne 2022 = 51:07
IJ8Yb1uMZKA = 8 months ago = Interviewing like a Boss - Kris Howard - NDC Melbourne 2022 = 1:01:48
x79xykhpBNo = 8 months ago = Demystifying Azure AD, JWTs & OIDC - Graeme Foster - NDC Melbourne 2022 = 1:01:48
I2_-czgGAls = 8 months ago = Chasing the holy grail  Reusable Web Components and Design Tokens - Duncan Hunter = 56:28
G1iL9JYBywY = 8 months ago = Building Airplanes in the Sky with Serverless and Low Code - Todd Whitehead - NDC Melbourne 2022 = 47:21
0JezWEaSQ8k = 8 months ago = Working in the industry as a PhD graduate - Sahar Sohrabi - NDC Melbourne 2022 = 14:47
K5QzxzuGsDw = 8 months ago = How to write better legacy code: A developer's wishlist - Bhaman Nikkahan - NDC Melbourne 2022 = 21:38
czC2DcTHYxY = 8 months ago = GitHub like a Boss - Michelle Mannering - NDC Melbourne 2022 = 49:31
3AZFMT0LNAU = 8 months ago = PICKUP DATA: A Kafka Adventure Game - Kris Jenkins - NDC Melbourne 2022 = 46:39
GZD9cfPFJxs = 8 months ago = Hello AI World! - Why Developers Should Care About AI - Matthew Renze - NDC Melbourne 2022 = 59:50
QZ2WhkjaCV0 = 8 months ago = Making neural networks run in browser with ONNX - Ron Dagdag - NDC Melbourne 2022 = 50:44
XphKVz0xX64 = 8 months ago = The Modern Trolley Problem - Michelle Sandford - NDC Melbourne 2022 = 59:10
XzJlq_XrlCI = 9 months ago = Understanding the Cyber Security Acronym Soup - Kieran Jacobsen - NDC Melbourne 2022 = 50:45
XDJ7_UvRjis = 9 months ago = Diamonds are forever, so are URLs - Wing Ho - NDC Melbourne 2022 = 13:05
I7n797EMeJU = 9 months ago = DevOps Pitfalls, Beyond The Technology - Emad Alashi - NDC Melbourne 2022 = 10:44
0_ZhiNnxEsA = 9 months ago = Avoiding DNS Pain - Kieran Jacobsen - NDC Melbourne 2022 = 9:56
CwTFVvSC2N0 = 9 months ago = 210 x 297   UX Design for the Physical World - Rebecca Platt - NDC Melbourne 2022 = 13:06
bl7wFMwboBM = 9 months ago = eXential XSS (Cross Site Scripting) - Alex Mackey - NDC Melbourne 202 = 1:02:06
dgyk7zkttHI = 9 months ago = Coding in the Cloud with GitHub Codespaces - Damian Brady - NDC Melbourne 2022 = 57:39
zyjwHJwzHB8 = 9 months ago = Entity Framework Core Unchained  Getting the Best Performance from Your ORM - Dan Mallott = 1:00:40
2tizzywjIUw = 9 months ago = IP Allow lists suck  Secure your staging environments with Cloudflare workers - Klee Thomas = 55:58
9uKve5hq9kY = 9 months ago = Bicep: Deploy to Azure cloud without it being a pain in the Arm - Paul Glavich - NDC Melbourne 2022 = 1:02:26
I5kx__o4S3k = 9 months ago = Unleash the Power of Visual Studio Code - Aaron Powell - NDC Melbourne 2022 = 59:21
qSFBC5X72_c = 9 months ago = Refactoring Components - Erin Zimmer - NDC Melbourne 2022 = 49:36
4W_LnDLigds = 9 months ago = Banking on Australia as a tech nation - James Wilson - NDC Melbourne 2022 = 58:14
qz_ulWea7nc = 9 months ago = Practical Pipelines  A Houseplant Soil Alerting System with ksqlDB - Danica Fine - NDC Melbourne 202 = 52:41
o6cK-m-2stg = 9 months ago = Space in the 2020's - Richard Campbell - NDC Melbourne 2022 = 1:10:06
avEHsz9y918 = 9 months ago = Defensive Coding Bootcamp - Heather Downing - NDC Melbourne 2022 = 50:59
_tRa4Mg3sqg = 9 months ago = NET Everything - Melissa Houghton - NDC Melbourne 2022 = 49:50
A_gtQs0OLH0 = 9 months ago = Deploying Cloud Infrastructure using Pulumi - Shahid Iqbal - NDC Melbourne 2022 = 58:18
KrtXD7yc_Ek = 9 months ago = Engineering for Low Code Solutions - Andrew Coates - NDC Melbourne 2022 = 57:07
jJ3tYhO8uuQ = 9 months ago = Type safe GraphQL with TypeScript - Aaron Powell - NDC Melbourne 2022 = 56:40
PFeGlsorZFk = 9 months ago = Pipelines, IaC and Deployments with Github Actions & Octopus Deploy - Derek Campbell - NDC Melbourne = 42:07
f0LDGkHQuUs = 9 months ago = Containers for dotnet developers - Jorge Arteiro - NDC Melbourne 2022 = 1:03:23
JQL4doMy73w = 9 months ago = How to Close the Diversity Gap - Heather Wilde - NDC Melbourne 2022 = 1:01:40
w5MKY9rOHi4 = 9 months ago = What's new in C# 11 now with less controversy!! - David Wengier - NDC Melbourne 2022 = 58:18
jOOFrCFuveA = 9 months ago = How to Build a Quokkabot - Amy Kapernick - NDC Melbourne 2022 = 55:19
BVJVhceN3N4 = 9 months ago = Developing Flexible Authorisation Capabilities in ASP NET Core - Jason Taylor - NDC Melbourne 2022 = 51:21
htr-qfggJtc = 9 months ago = Beyond Sentiment Analysis: Object Detection with ML NET - Arafat Tehsin - NDC Melbourne 2022 = 58:33
ObycG5T4urc = 9 months ago = NDC London 2023 - Conference for Software Developers = 0:29
Xtihes__kpw = 9 months ago = 10 Tips to Rocking as an Azure Architect - Adam Cogan - NDC Melbourne 2022 = 57:21
AZgKO4SQ6gM = 9 months ago = #ndcoslo #shorts = 1:01
OfZ_EkGkOGU = 9 months ago = Scalable Microservices with gRPC & Kubernetes - Sanket Singh - NDC Melbourne 2022 = 59:54
BSGkTH--4j8 = 9 months ago = One Step Deeper in Dapr's Pub:Sub - Emad Alashi - NDC Melbourne 2022 = 50:09
ASs3_FUx2GE = 9 months ago = Web APIs for delightful two factor auth experiences - Phil Nash - NDC Melbourne 2022 = 50:58
i6KiPww_pRA = 9 months ago = Event driven architectures on Azure - Graeme Foster - NDC Melbourne 2022 = 56:47
inzVR7FQ4nU = 9 months ago = Azure and Containers, the tale of the two inseparable friends - Yaser Adel Mehraban - NDC Melbourne = 43:53
FhIWCuup2EA = 9 months ago = Locks are tricky — let's understand them by building one - Adam Furmanek   NDC Melbourne 2022 = 1:05:30
-gWgxWHkBGg = 9 months ago = A11y on the back end - Samuel Levy - NDC Melbourne 2022 = 1:16:15
lfZU98rtnLE = 9 months ago = Learning from Disaster - Ian Hughes - NDC Melbourne 2022 = 1:00:04
9-pDneq5NiI = 9 months ago = I fought the law and the law won - Hackle Wayne - NDC Melbourne 2022 = 46:29
ifx_7daOzZw = 9 months ago = Using C# Source Generators to Build a .NET IoT Device - Alon Fliess - NDC Melbourne 2022 = 59:51
GS16Hyad-i0 = 9 months ago = Kill All Mutants! Intro to Mutation Testing - Dave Aronson - NDC Melbourne 2022 = 49:46
00HGqvsF-94 = 9 months ago = From Rags to Revenue: 5 years of a developer startup - Ben Cull - NDC Melbourne 2022 = 1:00:31
vcRkaNdzWa4 = 9 months ago = The Curious Incident in your Software in the Day Time - Liam Westley - NDC Melbourne 2022 = 56:52
MoV4nPNHO1M = 9 months ago = GitHub Actions - CI:CD and more - Damian Brady - NDC Melbourne 2022 = 54:46
tqagEuHYSys = 9 months ago = Video Analytics for mere mortals with NVIDIA DeepStream SDK - Yousry Mohamed - NDC Melbourne 2022 = 52:55
e1bwPonKRMc = 9 months ago = A web for anyone, anywhere, anytime - Rowdy Rabouw - NDC Melbourne 2022 = 1:06:43
LQmq9-drDVk = 9 months ago = Fractal Architecture - Mark Seemann - NDC Melbourne 2022 = 1:02:28
O0sCk-GiFIQ = 9 months ago = Always crashing in the same car (the state of front end web development in 2022) - William Tulloch = 57:55
a-iW7ykePbA = 9 months ago = Building Skills and Creating Communities - Donna Edwards - NDC Melbourne 2022 = 45:02
sLdFcxFwS0c = 9 months ago = End to End DevOps with GitHub - Damian Brady - NDC Melbourne 2022 = 47:40
reL-ke2J03o = 9 months ago = Keynote - The Next Decade of Software Development - Richard Campbell - NDC Melbourne 2022 = 1:06:50
HlubhN0BG1w = 10 months ago = The Adoption and Operation of Serverless at LEGO.com - Sheen Brisals & Luke Hedger = 1:16:27
ltUbn6SBbUc = 10 months ago = The Return of the Authentication Cookie - Anders Abel - NDC Copenhagen 2022 = 1:02:15
XIdLmf9MtX8 = 10 months ago = JSON over HTTP Multiple Ways - Poornima Nayar - NDC Copenhagen 2022 = 49:21
d---qZprdfk = 10 months ago = Supercharge your Kubernetes Ingress with Kong Ingress Controller - Viktor Gamov - NDC Copenhagen = 57:33
Retjj8_O9JE = 10 months ago = GraphQL Observability with Elastic and OpenTelemetry - Michael Staib - NDC Copenhagen 2022 = 51:38
iBfAA2AuaGk = 10 months ago = NDC TechTown 2022 = 1:01
Ak1hGQuGBhY = 10 months ago = Repeatable Execution - Mark Seemann - NDC Copenhagen 2022 = 1:00:07
VOZGO1jb0oM = 10 months ago = Lean & Lego: Building the Millennium Falcon Redux - James Lewis - NDC Copenhagen 2022 = 57:09
c59z9LFkNqU = 11 months ago = Micro-frontend magic in a regulated environment - James Strachan & Nikola Kovačević = 1:01:29
qC_ioJQpv4E = 11 months ago = Programming’s Greatest Mistakes - Mark Rendle - NDC Copenhagen 2022 = 55:35
3JnMfJM9K0c = 11 months ago = Distributed Tracing in .NET 6 using OpenTelemetry - Martin Thwaites - NDC Copenhagen 2022 = 56:53
V4zqk4-LL1M = 11 months ago = Automate yourself out of a job with Roslyn - Mark Rendle - NDC Copenhagen 2022 = 1:03:52
v8bqAm4aUFM = 11 months ago = Where’s C# headed? - Mads Torgersen - NDC Copenhagen 2022 = 1:01:28
FPEEiX5unWI = 11 months ago = Fractal Architecture - Mark Seemann - NDC Copenhagen 2022 = 59:42
CLKZ7ZgVido = 11 months ago = The functional journey of C# - Mads Torgersen - NDC Copenhagen 2022 = 1:01:28
2o44zNEi5bA = 11 months ago = XSS History and Conclusion - Jim Manico = 13:38
awVCTAnR76k = 11 months ago = OWASP Project History - Jim Manico = 3:02
YXH77EpJ9wk = 11 months ago = Who tests their cloud code anyway? - Lars Klint - NDC Copenhagen 2022 = 58:44
ne6D_QFlcCI = 11 months ago = How to Customize your Terminal - Scott Hanselman = 4:28
rUP1Hl9jrQg = 11 months ago = NDC Minnesota - 15-18 Nov 2022 - 4-Day Workshop Event for Software Developers = 1:00
NqnCFQaEgUU = 11 months ago = Password History - Jim Manico = 7:17
iw5kT9NoYAQ = 11 months ago = .NET Developer? You're an IoT Developer Too! - Rob Lauer - NDC Copenhagen 2022 = 39:29
7xsygqaQKJg = 11 months ago = Powering the Front-end with React, GraphQL and Relay - Martin Artola - NDC Copenhagen 2022 = 1:02:53
SQXGR6VENXA = 11 months ago = Stretching for Zero Downtime Upgrades in Azure - Sven Malvik - NDC Copenhagen 2022 = 49:30
2cZpC94P2Pw = 11 months ago = The Developer's Guide to Data Modelling with Document Databases - Adrienne Braganza Tacke = 53:50
fFpFdD3ExFo = 11 months ago = Yarn Berry: a next generation package manager - Michael Richardson - NDC Copenhagen 2022 = 54:53
nVhNpXBLCL8 = 11 months ago = Serverless landscape beyond functions - Mete Atamel - NDC Copenhagen 2022 = 53:44
cpsgAQFkhCE = 11 months ago = Elasticsearch Under the Hood - Philipp Krenn - NDC Copenhagen 2022 = 57:55
fYFruezJEDs = 11 months ago = Async Code Reviews Are Killing Your Company’s Throughput - Dragan Stepanović - NDC Copenhagen 2022 = 43:28
d-bN0uYuwck = 11 months ago = Machine Learning in the Real World - Karsten Strøbæk - NDC Copenhagen 2022 = 57:05
CmdRUzdpkkg = 11 months ago = Flow Engineering, boost velocity, quality & happiness through your value stream - Steve Pereira = 1:01:22
Vk2fi7NZ3OQ = 11 months ago = Failure is Always an Option - Dylan Beattie - NDC Copenhagen 2022 = 47:44
HY0NX69LOAg = 11 months ago = How to Effectively Move from Ideation to Implementation - Amber Vanderburg - NDC Copenhagen 2022 = 58:16
Bs36hmTy7Y4 = 11 months ago = Kubernetes and Selenium Grid for highly scalable browser and device farm - Ragavan Ambighananthan = 49:41
rlRNsCGQlOg = 11 months ago = Building beautiful Blazor apps with Tailwind CSS - Chris Sainty - NDC Copenhagen 2022 = 1:01:45
uKV31NImnuI = 11 months ago = Evolving your APIs, a Pragmatic Approach - Nicolas Fränkel - NDC Copenhagen 2022 = 58:13
i16jemxwCr8 = 11 months ago = Design & Reality - Mathias Verraes - NDC Copenhagen 2022 = 53:27
6vBj6j6t4ag = 11 months ago = Codezillas: The Universal Truths of Building Trust - Nathaniel Schutta & Whitney Lee = 1:00:28
qrh97hToWpM = 11 months ago = Getting started with GraphQL in .NET - Michael Staib - NDC Copenhagen 2022 = 59:11
E7CufNR84M4 = 11 months ago = Build Automation Revolution with NUKE - Matthias Koch - NDC Copenhagen 2022 = 52:58
gd5uJ7Nlvvo = 11 months ago = Plain Text - Dylan Beattie - NDC Copenhagen 2022 = 59:20
0ial6pfgV9g = 11 months ago = Hacking C#: Development for the Truly Lazy - Simon Painter - NDC Copenhagen 2022 = 50:25
uAwJEFLJunk = 11 months ago = Keynote: Software Architecture, Team Topologies and Complexity Science - James Lewis = 56:33
Zj16hGst-tw = 11 months ago = NDC Minnesota Workshop: Identity & Access Control for modern Applications and APIs - Brock Allen = 1:18
EzGMFZaTnk8 = 11 months ago = NDC Minnesota Workshop: Reactive Mobile Apps with GraphQL and Maui - Michael Staib & Bradon Minnick = 1:06
kJFB8o78FBs = 11 months ago = NDC Minnesota Workshop: Introduction to Effective testing in C# and .NET - Nick Chapsas = 0:41
0x23k6tTU7k = 11 months ago = Managing Event Driven Architectures - Ian Cooper - NDC London 2022 = 1:00:34
XEdB4G4HBls = 11 months ago = Automated Canary Deployments with HashiCorp Consul - Nic Jackson & Erik Veld - NDC London 2022 = 54:17
lcGf2Txq92o = 11 months ago = Actors can rule your DDD world - Hannes Lowette - NDC London 2022 = 59:07
R3u4Gb7mazE = 11 months ago = Back to Basics: Efficient Async and Await - Filip Ekberg - NDC London 2022 = 1:01:59
nLxSzZF8VVo = 11 months ago = Practical tips to elevate your UX and accessibility - Jessica Engström - NDC London 2022 = 54:41
0FnJeikULJU = 11 months ago = Having fun with Generics and Abstract classes in C# - Don Wibier - NDC London 2022 = 57:54
sBbg0ow3hh0 = 11 months ago = Real-time Machine Learning with Pulsar Functions - David Kjerrumgaard - NDC London 2022 = 54:33
mo0ukBw4nZE = 11 months ago = JavaScript Metaprogramming - Dave Fancher - NDC London 2022 = 58:26
wOq9meKcdlw = 11 months ago = Real-Time Revolution: SignalR in Action - Kevin Griffin - NDC London 2022 = 1:06:04
PR3U9RjpmRc = 11 months ago = DevOps for Databases - Scott Sauber - NDC London 2022 = 57:31
s-xaBcVdxLY = 11 months ago = Introducing the Windows App SDK - Nico Vermeir - NDC London 2022 = 1:02:45
hy_GWqjia3U = 11 months ago = Azure Functions: a guide to getting started - Layla Porter - NDC London 2022 = 55:26
EWI7rFL8L0s = 11 months ago = You Shall Not Password: Modern Authentication for Web Apps - Eli Holderness - NDC London 2022 = 37:18
oD71pQNrc0Q = 11 months ago = Building AI enriched applications with Azure Cognitive Search and CosmosDb - Glenn Colpaert = 53:38
D7LKslgwxmQ = 11 months ago = Test Driven Development in JavaScript – writing tests that don’t suck! - David Whitney = 54:20
q_6NRHXAK_Y = 11 months ago = ASP.NET Core Beyond the Basics - Chris Klug - NDC London 2022 = 59:27
kcFJtRRNG3c = 11 months ago = Practical tips and tricks for CI/CD success - Zan Markan - NDC London 2022 = 21:29
snGieEdIdMs = 11 months ago = What I learnt about Containers - Graham Chukwumaobi - NDC London 2022 = 13:40
BtuhWG2Yx08 = 11 months ago = Good Writers Become Better Developers - Rizwana Akmal Khan - NDC London 2022 = 10:39
849QdYnT5S8 = 11 months ago = Marvels of Teenage Engineering - Anders Norås - NDC London 2022 = 43:48
k0URnQ01064 = 11 months ago = Handling Application State in Blazor - Carl Franklin - NDC London 2022 = 41:45
dbJaijxPli4 = 11 months ago = Building beautiful Blazor apps with Tailwind CSS - Lemon - NDC London 2022 = 57:13
GKbTgovP-VU = 11 months ago = Building beautiful Blazor apps with Tailwind CSS - Chris Sainty - NDC London 2022 = 55:30
4uyr-0cMY84 = 11 months ago = You're on mute! WebRTC and our lives on screen - Liz Moy - NDC London 2022 = 36:52
WN3CSOai_ZU = 11 months ago = The Silver Bullet Syndrome Part 2 - Complexity Strikes Back! - Hadi Hariri - NDC London 2022 = 46:07
cM4CABxMmk8 = 11 months ago = Share Pie: The DDD Treasure Hidden in Plain Sight - Nick Tune - NDC London 2022 = 38:52
_oPzRQExVvM = 11 months ago = Mayday! Software lessons from aviation disasters - Adele Carpenter - NDC London 2022 = 47:10
jO5w1MwnxaM = 11 months ago = Cypress for developers who hate writing tests - Ruby Jane Cabagnot - NDC London 2022 = 43:34
gxOUXJz7PcM = 11 months ago = The Developer's Guide to Data Modelling with Document Databases - Adrienne Braganza Tacke = 38:05
ONKTFbzwqE0 = 11 months ago = Building your personal online brand using Static Blazor Apps, one step at a time - Stacy Cashmore = 58:07
yA-b-V_9N_E = 11 months ago = Advanced .NET debugging - Tess Ferrandez-Norlander - NDC London 2022 = 50:44
AT6-WXLwKQE = 11 months ago = I don’t want to miss a Thing 🎶 - Track Database Changes with Apache Kafka - Francesco Tisiot = 53:37
xYvLgW3vGiE = 11 months ago = GraphQL Observability with Elastic and OpenTelemetry - Michael Staib - NDC London 2022 = 56:08
WIq9pd-S-D4 = 11 months ago = How the fastest growing companies develop their public API - Josh Twist - NDC London 2022 = 56:11
1jHuZpz_Wpc = 11 months ago = Controlling My Home Sauna Using .NET 6 and MAUI - Johnny Hooyberghs - NDC London 2022 = 56:35
yqRVFWBm2Hg = 11 months ago = Build Team Relationships & Push Through Conflicts with Nonviolent Communication - Jenny Martin = 48:01
C2uaittXEEc = 11 months ago = Empower your Azure IaC with Bicep! - Eldert Grootenboer - NDC London 2022 = 55:28
UmBzJ5pBpqQ = 11 months ago = Open source for fun and profit: rethinking the long road of sustainability - Tania Allard = 55:25
UXQHREbSV-0 = 11 months ago = Measuring DevSecOps - Victoria Almazova - NDC London 2022 = 33:05
U7hQ6JGetvM = 11 months ago = User Experience Pitfalls - Ash Banaszek - NDC London 2022 = 43:06
H5QCejO8_rE = 11 months ago = Making sense of unstructured data with AI - Henk Boelman -  NDC London 2022 = 59:34
eNbzSg_44tU = 11 months ago = Tailwind CSS: A Different Approach to Styling Websites - Shawn Wildermuth - NDC London 2022 = 53:03
Hi6ICEVVRiw = 11 months ago = Concurrent Affairs: Procedural Programming Unlocked - Kevlin Henney - NDC London 2022 = 1:05:20
YcZ-nZa2XgA = 11 months ago = Performance in the .NET Runtime - Matt Warren - NDC London 2022 = 58:57
HqwY_TyxeJw = 11 months ago = Dungeons, Dragons, and Graph Databases - Guy Royse - NDC London 2022 = 1:00:34
mlGdFB_bCE4 = 11 months ago = Awesome Azure Authentication Adventures - Glenn F. Henriksen - NDC London 2022 = 1:02:42
NqTVANK7Mg8 = 11 months ago = Commodore 64 Emulation in JavaScript - Imran Nazar - NDC London 2022 = 16:05
Cnhvk-2LcJ8 = 11 months ago = Software developers are roller coaster addicts? - Johnny Hooyberghs - NDC London 2022 = 23:18
n9_dqtDy-2U = 11 months ago = Securing your .NET application software supply-chain - Niels Tanis - NDC London 2022 = 56:33
xrt9Q2TMlYA = 11 months ago = Design for Developers - Lex Lofthouse - NDC London 2022 = 55:23
f64tZ90Dntg = 11 months ago = Domain-Driven Refactoring - Jimmy Bogard - NDC London 2022 = 1:00:03
E_4vo8fSNeU = 11 months ago = How to be Fast: A Look at High Performance Websites - Eric Brandes - NDC London 2022 = 37:49
bEYkIhHLDmM = 11 months ago = Fractal architecture - Mark Seemann - NDC London 2022 = 54:31
okoc27gGw8E = 11 months ago = End the "WOrKs on My MAcHiNe!" Nightmare With CS Code and Dev Containers - Rob Conery = 42:44
Av3QP940L2c = 11 months ago = Failure is Always an Option - Dylan Beattie - NDC London 2022 = 50:28
SR53SKIUYPA = 11 months ago = Building a microservice architecture with ASP.NET Core - Gill Cleeren - NDC London 2022 = 56:52
35raD4Rfl1g = 11 months ago = Move your dev environment to the cloud with GitHub Codespaces - Jakob Ehn - NDC London 2022 = 55:28
f9p6iA2rB58 = 11 months ago = What's new in C#? Exciting new features in C# 8.0, 9.0 and 10! - Filip Ekberg - NDC London 2022 = 1:02:34
C_2BStepVKw = 11 months ago = PM on the NuGet team at Microsoft - Claire Novotny - NDC London 2022 = 1:04:37
GzVi_YYdfoY = 11 months ago = .NET on tiny IOT Meadow Boards - Clifford Agius - NDC London 2022 = 52:47
ZKVXl2640ps = 11 months ago = Entity Framework (Core) Unchained: Getting the Best Performance from Your ORM - Dan Mallott = 44:03
_mbsMKymGjk = 11 months ago = An Introduction to Elasticsearch for .NET Developers - Steve Gordon - NDC London 2022 = 59:56
LNnrebfptLk = 11 months ago = The Curious Incident in your Software in the Day-Time - Liam Westley - NDC London 2022 = 1:00:22
5s3CpxjvlrY = 11 months ago = Zero to Document Hero - Intro to MongoDB and .NET - Luce Carter - NDC London 2022 = 52:28
JSTx42SxCcg = 11 months ago = Pipelines, IaC and Deployments with Github Actions & Octopus Deploy - Derek Campbell = 32:54
UVw1-Y404bU = 11 months ago = The Untruthful Art - Five Ways of Misrepresenting Data - Alexander Arvidsson - NDC London 2022 = 57:11
tL5e_ONnC9c = 11 months ago = How Product Manufacturing Can Teach us to Write Better Software - Stephen Haunts -  NDC London 2022 = 49:11
ju5feVtP2a0 = 11 months ago = Indexing, Searching, and Aggregation with RediSearch and .NET - Steve Lorello - NDC London 2022 = 54:14
5cMqRfp-Bmo = 11 months ago = The Visible Developer: Why You Shouldn't Blend In - Heather Downing - NDC London 2022 = 52:59
n2kOPiEFqPs = 11 months ago = Let's Talk About Web Components - Jemima Abu -  NDC London 2022 = 40:39
mIa5aS7cTig = 11 months ago = Serverless Patterns Made Simple with Real World Usecases - Sheen Brisals - NDC London 2022 = 1:02:47
aryVbnvPbVg = 11 months ago = A 101 in Time Series Data - Jay Clifford - NDC London 2022 = 1:06:54
M6h-rpbvJB4 = 11 months ago = Why you should consider Web Assembly in your next frontend project - Håkan Silfvernagel = 39:14
jICikVZJJJU = 11 months ago = The global future of work - inspiration/ insight from emerging markets - Charles Sekwalor = 49:19
_Qzc0PgWEs8 = 11 months ago = Nitty-Gitty: Master Git from the Inside - Manu Magalhães - NDC London 2022 = 47:18
TtI8X25bPn8 = 11 months ago = Catching Scammers on Kafka streams with Graphs - Ebru Cucen - NDC London 2022 = 11:30
xEGVHVzD4HE = 11 months ago = Brewing Tea Over HTTP - Imran Nazar - NDC London 2022 = 11:51
APCOWwg9YDs = 11 months ago = API design for Front-end engineers - Teresa Wu -  NDC London 2022 = 10:17
eMLD77rqUJc = 11 months ago = Integration, integration, integration - Jon Skeet - NDC London 2022 = 1:06:00
KRLOCFDw5x4 = 11 months ago = CUPID - for joyful coding - Daniel Terhorst-North - NDC London 2022 = 1:01:15
hPpvlKLeYYA = 11 months ago = Goodbye controllers, hello Minimal APIs - Nick Chapsas - NDC London 2022 = 52:02
JdOoHmCLrM8 = 11 months ago = Observable Web Applications - Todd Gardner - NDC London 2022 = 51:49
lm1GqG4eIDA = 11 months ago = Building a wearable live captioning display to help - Jo Franchetti - NDC London 2022 = 35:32
RevmsFXVJ5Q = 11 months ago = Making Blazor work with everything, plus WebAssembly on the server - Steve Sanderson = 1:00:22
-8mQl76mQ8w = 11 months ago = Lean & Lego: Building the Millennium Falcon Redux - James Lewis - NDC London 2022 = 54:56
Ks13Qa5HtWw = 11 months ago = Build powerful distributed applications with Dapr and .NET - Rodrigo Díaz Concha - NDC Porto 2022 = 1:06:13
mqUVVBy057E = 11 months ago = From Flatland to Spaceland - Rafał Legiędź - NDC Porto 2022 = 55:44
b0G0FW5-q0U = 11 months ago = Sandboxing .NET assemblies for fun, profit and of course security! - Niels Tanis -  NDC Porto 2022 = 53:46
IchbB9nQWps = 11 months ago = Blazing Accessibility Basics - Dennie Declercq - NDC Porto 2022 = 56:18
GSZpcKyXa6k = 11 months ago = It’s easy to create a good looking product, but what about a useful one? - Eleftheria Batsou = 28:19
mTqa0FkaSus = 11 months ago = Testing in Production - Talia Nassi - NDC Porto 2022 = 21:33
g6cl7wv6QYw = 11 months ago = Functional Programming with C# - Simon Painter - NDC Porto 2022 = 58:10
R1r1VMYVXG0 = 11 months ago = Deep dive into Durable Functions - Laurent Bugnion - NDC Porto 2022 = 58:22
dAkloM5RHKQ = 11 months ago = Now THAT'S What I Call Service Worker! - Jeremy Wagner - NDC Porto 2022 = 50:19
9AGKH1VKuW0 = 11 months ago = Embracing gRPC in .NET - Irina Scurtu - NDC Porto 2022 = 54:49
4zAb3vKC2Fk = 11 months ago = Achieving great API-ness. Why streaming and API management go hand in hand - Ljubica Lazarevic = 35:03
QMJ8vH2ubQ8 = 11 months ago = Making Every Game More Accessible with .NET and AI - Alex Dunn - NDC Porto 2022 = 42:12
DkHpCnLTyR4 = 11 months ago = Mixing Paradigms Using the Latest C# Language Features - Zoran Horvat - NDC Porto 2022 = 1:02:40
fYs3tf7RHIQ = 11 months ago = Come listen to me, I’m a fraud! A story on success - Joep Piscaer - NDC Porto 2022 = 36:33
PtRCCj8tHWM = 11 months ago = The Bizarre Quantum World with Q# and Azure Quantum - Filip W - NDC Porto 2022 = 58:34
9fb9MSDsY3A = 11 months ago = Change wings on the fly - Tatiana Kolesnikova - NDC Porto 2022 = 46:17
SEGzUdK-Oas = 11 months ago = The Art of Documentation and Readme.md - Ben Hall - NDC Porto 2022 = 47:14
qAdJ3SNEBBo = 11 months ago = Embrace chaos to achieve stability - René van Osnabrugge - NDC Porto 2022 = 1:01:28
Q6cWn4HO3wQ = 11 months ago = Application security from start to finish - Michael Kaufmann - NDC Porto 2022 = 45:56
B_i6-K03An0 = 11 months ago = Migrating your messaging workloads to the Cloud with Azure Service Bus - Eldert Grootenboer = 49:51
L9p-9dGp-98 = 11 months ago = State management in Blazor - Don Wibier - NDC Porto 2022 = 1:02:43
xUhwnwRrYPk = 11 months ago = Learning about machine learning from kids - Dale Lane - NDC Porto 2022 = 36:04
b5DV_coRBUU = 11 months ago = Minimal APIs in ASP.NET 6.0 - Rob Richardson - NDC Porto 2022 = 53:55
r226vtO--B4 = 11 months ago = Space Flight in the 2020s - Richard Campbell - NDC Porto 2022 = 56:36
AQb0LsbmJME = 11 months ago = Smart home from scratch - a little C#, a little C++ and cheap Chinese electronics - Nir Dobovizki = 50:59
1xuv7uOnK00 = 11 months ago = The Care and Feeding of Software Engineers - Heather Downing - NDC Porto 2022 = 1:01:10
gHSpj2zM9Nw = 11 months ago = The Grand Unified Theory of Clean Architecture and Test Pyramid - Guilherme Ferreira - NDC Porto = 50:16
xgSmPu_rB3w = 11 months ago = Leadership Lessons from the Agile Manifesto - Anjuan Simmons - NDC Porto 2022 = 1:01:16
EMgofGN4xEQ = 11 months ago = Exploring the Wonderful World of Python on Devices - Brandon Satrom - NDC Porto 2022 = 39:12
dd9MCsDlpOY = 11 months ago = Open Source at commercial organisations - Daniel Albuquerque & Nikos Katirtzis - NDC Porto 2022 = 56:55
wRC7jyhTkEM = 11 months ago = The Last XSS Defense Talk - Jim Manico - NDC Porto 2022 = 57:24
5FQ83PsCCGY = 11 months ago = Realities & Misconceptions about Enterprise Applications of AI/ML and Data - Brooke Jamieson = 50:17
4JrrRaWMzQI = 11 months ago = Implementing async with coroutines and fibers - project Loom in C# - Adam Furmanek - NDC Porto 2022 = 1:04:44
ISuScsCeadU = 11 months ago = Auditing your data and answering the question, is it the end of the day yet? - Simona Meriam = 37:12
QgwP3QdSKkg = 1 year ago = Impactful mentorship - Eldert Grootenboer & Olena Borzenko - 2 sides of a story - NDC Porto 2022 = 37:01
I76uhPaWY1o = 1 year ago = Embracing Simplicity - Guilherme Ferreira - NDC Porto 2022 = 47:48
P96CByrJNxk = 1 year ago = Top new CNCF projects to look out for - Annie Talvasto - NDC Porto 2022 = 45:48
b6YLorczub8 = 1 year ago = The Developer's Guide to Data Modelling with Document Databases - Adrienne Braganza Tacke = 43:52
147txqwmvNQ = 1 year ago = DevOps transformation – the good, the bad and the ugly - Todor Todorov - NDC Porto 2022 = 37:37
YWX-taj2iH0 = 1 year ago = The definitive deep dive into the .git folder - Rob Richardson - NDC Porto 2022 = 1:06:30
oBl9CDK9wqU = 1 year ago = Relia...bility? - Ricardo Castro - NDC Porto 2022 = 36:32
NdScMUT4qlE = 1 year ago = Scaling Reliability Engineering with Tools - Nikos Katirtzis & Daniel Albuquerque - NDC Porto 2022 = 41:08
dX69x-D6COI = 1 year ago = Uno Platfrom: Your Apps Everywhere - Martin Zikmund - NDC Porto 2022 = 58:10
gkAx6zfMICA = 1 year ago = How Farfetch is facing the Cloud cost challenge - Anderson Oliveira - NDC Porto 2022 = 57:55
yIaJgSSVCfw = 1 year ago = Supporting your peers' growth as a tech lead - Alon Kiriati - NDC Porto 2022 = 49:53
9IU2gsZ15Lw = 1 year ago = Share Pie: The DDD Treasure Hidden in Plain Sight - Nick Tune - NDC Porto 2022 = 32:24
3jX6AOW1y-g = 1 year ago = Building modern applications with GraphQL 2021 and beyond in ASP.NET Core 6 - Michael Staib = 57:22
oALRmk0YohU = 1 year ago = A gentle introduction to Deep Learning - Laurent Bugnion - NDC Porto 2022 = 1:00:04
EnqAPxr-uko = 1 year ago = Build and deploy production ready PyTorch models - Henk Boelman - NDC Porto 2022 = 59:12
unc5oAElDDw = 1 year ago = Cost cutting strategies for Azure Cosmos DB - Hasan Savran - NDC Porto 2022 = 59:38
xzRhabmlc8M = 1 year ago = Securing SPAs and Blazor Applications using the BFF (Backend for Frontend) Pattern - Dominick Baier = 56:53
DJZI-C_nrqQ = 1 year ago = Design & Development Considerations for Dual Screen Devices - Stephanie Stimac - NDC Porto 2022 = 32:34
nCLSfJMihsg = 1 year ago = GraphQL Observability with Elastic and OpenTelemetry - Michael Staib - NDC Porto 2022 = 51:49
rxI-ffJCTQ0 = 1 year ago = I'm Going To Make You Stop Hating CSS - Lemon 🍋 - NDC Porto 2022 = 57:15
H-Cyw2ZUFBk = 1 year ago = NDC Sydney - 10-14 Oct 2022 | Conference for Software Developers = 0:33
YVGILWeyhSs = 1 year ago = Not your Grandmother's On-Prem - Tomer Gabel - NDC Porto 2022 = 51:50
cYP8TcokSFI = 1 year ago = Streaming three ways with Blazor: REST, gRPC, and SignalR - Carl Franklin - NDC Porto 2022 = 45:31
Jivp9jFfgrs = 1 year ago = Let's Talk About Web Components - Jemima Abu - NDC Porto 2022 = 45:08
uQsT3n1NTkE = 1 year ago = Building beautiful Blazor apps with Tailwind CSS - Chris Sainty - NDC Porto 2022 = 58:57
MVNDppCzxUc = 1 year ago = Event Sourcing - what could possibly go wrong? - Andrzej Ludwikowski - NDC Porto 2022 = 47:54
YzCuxVGfq5g = 1 year ago = Mocking in Front-end and Back-end TypeScript Tests - Rob Richardson - NDC Porto 2022 = 46:39
eODDN0u5tnw = 1 year ago = Looking Back - The Last Twenty Years of Software Development - Richard Campbell - NDC Porto 2022 = 1:01:14
73R7vQ2zXP8 = 1 year ago = Secure Open Source Practices - Jillian Ratliff - NDC Porto 2022 = 29:44
84z7uJYUMOs = 1 year ago = What's new in C#? Exciting new features in C# 8.0, 9.0 and 10! - Filip Ekberg - NDC Porto 2022 = 1:02:37
Ps8ep-glDfc = 1 year ago = OAuth – the good Parts - Dominick Baier - NDC Porto 2022 = 57:50
HnbhS8-WEr8 = 1 year ago = How Product Manufacturing Can Teach us to Write Better Software - Stephen Haunts - NDC Porto 2022 = 50:34
WDd1QSZBjHI = 1 year ago = Actors can rule your DDD world - Hannes Lowette - NDC Porto 2022 = 58:42
8AUa-48LaVs = 1 year ago = .NET Rocks Live – Modernizing .NET Applications - Richard Campbell, Carl Franklin & Mark Rendle = 1:00:06
0oXAZQBHH70 = 1 year ago = Automate yourself out of a job with Roslyn - Mark Rendle - NDC Porto 2022 = 1:16:07
Fnb_i7aLrWo = 1 year ago = NDC Oslo - 26-30 Sept 2022 | Conference for Software Developers = 0:33
UAsrW-fgAsg = 1 year ago = Lean & Lego: Building the Millennium Falcon Redux - James Lewis - NDC Porto 2022 = 49:06
p0bKMuBdpL8 = 1 year ago = Hustle and Flow - Ian Cooper - NDC Porto 2022 = 58:53
XEeeYTG3hUg = 1 year ago = Back to Basics: Efficient Async and Await - Filip Ekberg - NDC Porto 2022 = 1:02:00
Vs1DWYrw2Ps = 1 year ago = Fractals, Factories and Fast Food - Dylan Beattie - NDC Porto 2022 = 44:54
5GLSBAYPSvo = 1 year ago = Domain-Driven Design and Team Topologies for Product-led Organizations - Nick Tune - NDC Porto 2022 = 53:37
-1dTA2LDZ9w = 1 year ago = Hacking C# from the inside - how to do anything in .NET - Adam Furmanek - NDC Porto 2022 = 2:18:07
lP_qdhAHFlg = 1 year ago = What’s next for Blazor, and .NET on WASI - Steve Sanderson - NDC Porto 2022 = 1:00:49
mE-DGW0CcAk = 1 year ago = Moving 17 years of old legacy code and sites into the Cloud - Scott Hanselman - NDC Porto 2022 = 1:00:17
gxgKgMvPH9I = 1 year ago = Domain-Driven Refactoring - Jimmy Bogard - NDC Porto 2022 = 1:01:29
tuhzVDc0Slg = 1 year ago = Developing for Linux on Windows - Scott Hanselman - NDC Porto 2022 = 1:08:42
t3rSCpcJzm0 = 1 year ago = Fractal Architecture - Mark Seemann - NDC Porto 2022 = 53:32
bDG40Y1nPEk = 1 year ago = How to use GitHub Actions with Security in mind - Rob Bos - NDC Security 2022 = 56:28
4v7hhuLmRdU = 1 year ago = How to detect Malware in Encrypted Traffic Without Decryption - Christopher van der Made = 46:14
H6HZYZGuJbE = 1 year ago = Centralized Policy Management - Noaa Barki - NDC Security 2022 = 35:42
ce3VBNrzRSE = 1 year ago = Secure Coding Back to Basics - Erlend Oftedal - NDC Security 2022 = 59:16
TliwtyvgcJs = 1 year ago = Secure Data Exchange in Digital Government Context - Petteri Kivimäki - NDC Security 2022 = 46:04
P-f4rko5he8 = 1 year ago = HelseID - Dag Helge Østerhagen & Rune Andreas Grimstad - NDC Security 2022 = 1:02:40
SRXwTzPXYD4 = 1 year ago = Minimum Viable Security - David Melamed - NDC Security 2022 = 32:44
whhM_P7xMMU = 1 year ago = Breaking AES with side channel analysis - Turid Herland - NDC Security 2022 = 59:00
lDL4bQLupKk = 1 year ago = Demostrating Binary Exploitation - Marit Iren Rognli Tokle & Christian Resell - NDC Security 2022 = 22:17
R05XO0eN_E4 = 1 year ago = Vulnerabilities that Hide from your Tools - Jillian Ratliff - NDC Security 2022 = 40:55
f5Zn1-XNkSo = 1 year ago = Measuring DevSecOps - Victoria Alamzova - NDC Security 2022 = 47:00
pKP-nv2Oqdg = 1 year ago = Passwords are not going away - Per Thorsheim - NDC Security 2022 = 1:05:20
CSe2FNy7Rko = 1 year ago = Getting API Security Right - Philippe De Ryck - NDC Security 2022 = 53:13
5sjj9z8HCM8 = 1 year ago = ASP.NET Core Meets Owasp Top 10 - Anders Abel - NDC Security 2022 = 54:25
12rzwnsi1zg = 1 year ago = Sandboxing a Linux Application - Martin Ertsås - NDC Security 2022 = 1:01:40
ahWjyfWAdIk = 1 year ago = Common Python Coding Mistakes - Christopher van der Made - NDC Security 2022 = 59:17
B5IT9qVMonM = 1 year ago = It doesn't take much to be above average - Alexander Lystad - NDC Security 2022 = 47:43
vBtDrVl6vvo = 1 year ago = Opening The Playbook; What to do when you've been hacked - Heather Wilde - NDC Security 2022 = 1:00:45
IL3BJ87dHkc = 1 year ago = Why We Should Kill Saml2 - Anders Abel - NDC Security 2022 = 45:17
ESzu0sNaIyE = 1 year ago = Security Control Enhancements - Jim Manico - NDC Security 2022 = 52:21
ox6i9sWm90A = 1 year ago = API security for developers - Philippe De Ryck. -NDC Oslo workshop = 0:18
6EiC0QEULkc = 1 year ago = NDC Melbourne 2022 | Conference for Software Developers = 0:34
gEiT0xeXkO4 = 1 year ago = NDC TechTown 2022 | Software Conference for Product Development = 1:09
SXWMlilD82w = 1 year ago = HTTPS History - Jim Manico = 6:15
dZYiveyMWXg = 1 year ago = Protect your code with GitHub security features - Rob Bos - NDC Security 2022 = 57:46
00R1JGBQEJg = 1 year ago = Protect Yourself Against Supply Chain Attacks - Rob Bos - NDC Security 2022 = 1:02:00
etLfGtvTJ2M = 1 year ago = Hyper Speed: When Big Data Blooms - Scott Helme - NDC Security 2022 = 1:00:20
sUKpUPu151Q = 1 year ago = AppSec is Too Hard!? - Philippe De Ryck - NDC Security 2022 = 50:20
_ppWRRj4brI = 1 year ago = Sharing Health Information Through APIs - Steinar Noem - NDC Security 2022 = 1:00:37
EOYLK_mSX-0 = 1 year ago = Classic Vulnerabilities - Patricia Aas - NDC Security 2022 = 1:05:00
sMI-37eAlzU = 1 year ago = On Building Teams - Niall Merrigan - NDC Security 2022 = 56:21
XKGADGyWy0E = 1 year ago = Introduction to Security Testing History - Jim Manico = 9:29
FQHM-N59Tbc = 1 year ago = Cloud Hacking Scenarios - Michal Brygidyn - NDC Security 2022 = 36:05
j9e6okYJEyQ = 1 year ago = Gamify your Security - Jillian Ratliff - NDC Security 2022 = 48:24
NxTGOM1CMEw = 1 year ago = NDC London | 9-13 May 2022  | Conference for Software Developers = 0:30
AJtZGPuFCDs = 1 year ago = NDC Porto 2022 - Conference for Software Developers = 0:30
OjHIF8xUm2Q = 1 year ago = Move the needle - Eric Rabinovitch - NDC Sydney 2021 = 52:44
7-Vt-cg1aMQ = 1 year ago = Beyond Sentiment Analysis: Real Time Object Detection with ML NET - Arafat Tehsin - NDC Sydney 2021 = 54:42
eYD4qrXVCGo = 1 year ago = From Horror Story... to Fairy Tale - Michael Dowden - NDC Sydney 2021 = 55:44
yHebbLd5avI = 1 year ago = You're on Mute! WEBRTC and our lives on screen - Phil Nash - NDC Sydney 2021 = 49:51
FXMIbyMzNXQ = 1 year ago = A practical approach to operating Data Service tiers on Kubernetes - Rags Srinivas - NDC Sydney 2021 = 56:58
u_m3-LUJcpQ = 1 year ago = Local Development Techniques with Kubernetes - Rob Richardson - NDC Sydney 2021 = 43:37
nSDa5p9P8k0 = 1 year ago = Containers in Azure - Yaser Adel Mehraban - NDC Sydney 2021 = 1:02:54
ffWjxam9GS8 = 1 year ago = Implementing an Event Sourcing strategy on Azure - Olena Borzenko & Eldert Grootenboer - NDC Sydney = 58:21
Icxsiv1SB6k = 1 year ago = Next level Security for your Azure applications - Jan de Vries - NDC Sydney 2021 = 45:25
F9Nx5Ho8h6w = 1 year ago = Building Enterprise Microservices using Ocelot and Azure - Patrick Zhao - NDC Sydney 2021 = 55:57
VDTHaH8r9YM = 1 year ago = Unleash your inner CTO! - Rob Crowley - NDC Sydney 2021 = 1:00:19
Po-t9V4_lAQ = 1 year ago = Cloudy with a chance of mobile - Matt Goldman - NDC Syndey 2021 = 56:12
xgh9F_HcOFo = 1 year ago = Super fast transactions in low milli seconds using Cosmos DB and Redis - Bryden Oliver = 46:10
484zSsJR4d8 = 1 year ago = The Marvels of Teenage Engineering - Anders Norås - NDC Oslo 2021 = 57:41
vcFBwt1nu2U = 1 year ago = The Worst Programming Language Ever - Mark Rendle - NDC Oslo 2021 = 1:00:41
iuWL2acLvP4 = 1 year ago = Scaling Machine Learning Pipelines in Cloud - Salman Iqbal - NDC Oslo 2021 = 54:14
zS0y9krXO6E = 1 year ago = Building beautiful Blazor apps with Tailwind CSS - Chris Sainty - NDC Oslo 2021 = 54:50
9Nn0OkLQ9lM = 1 year ago = Building GraphQL APIs in C# - Brandon Minnick - NDC Oslo 2021 = 58:53
yFVk3D76wQw = 1 year ago = ClojureScript: Fun and productive web development with next level tooling - Christian Johansen = 49:19
UxrwfTchPJ8 = 1 year ago = Yarn Berry: a next generation package manager - Michael Richardson - NDC Oslo 2021 = 50:49
1C-0HH5cw8A = 1 year ago = Logging Apache Spark   How we made it easy - Simona Meriam - NDC Oslo 2021 = 13:04
EI7WEhJ4DCY = 1 year ago = Improve your IaC game in Azure with Template Specs - Børge Wiik - NDC Oslo 2021 = 11:48
2E4H2yg6yPc = 1 year ago = How do I start a sustainability community in my organisation - Sara Bergman - NDC Oslo 2021 = 9:31
AFa-P9tvag4 = 1 year ago = Securing your  NET application software supply chain - Niels Tanis - NDC Oslo 2021 = 57:45
d_SU5IOkhQU = 1 year ago = Whodunit? A performance murder mystery - Thomas Heartman - NDC Oslo 2021 = 44:06
IVdNZg9LicI = 1 year ago = Learnings from the Enterprise-level Kubernetes transformation at Elkjøp Nordic - Fredrik Klingenberg = 1:01:49
i0khx8R1XcE = 1 year ago = Managing your settings in a secure way using Azure App Configuration - Cecilia Wirén - NDC Oslo 202 = 45:31
5nQ00_z0hF4 = 1 year ago = Defence in depth as Code - Tobias Ahnoff & Martin Altenstedt - NDC Oslo 2021 = 50:27
0GQwtUYMpzU = 1 year ago = Deep dive in Durable Functions - Laurent Bugnion - NDC Oslo 2021 = 57:49
L1Zgfr6bFvA = 1 year ago = Rethinking Reactive Architectures - David Leitner - NDC Oslo 2021 = 54:54
LILGt_pHk9M = 1 year ago = Automating a service worker with Workbox 6 - Maxim Salnikov - NDC Oslo 2021 = 51:23
cGiLWfpj4hA = 1 year ago = Why you need an API, and what to do about it - Glenn Henriksen - NDC Oslo 2021 = 49:00
M4S5epTJAIo = 1 year ago = The Untruthful Art: Five ways of misrepresenting Data - Alexander Arvidsson - NDC Oslo 2021 = 55:42
JOZ9Mv876tQ = 1 year ago = Building Reliable Services at NRK TV - Einar Høst - NDC Oslo 2021 = 1:00:01
Co7QetPYiO4 = 1 year ago = Best practices unit testing Blazor components with bUnit - Egil Hansen - NDC Oslo 2021 = 54:30
o2Vqq_oHMB4 = 1 year ago = The Future is holographic - Scott Leaman - NDC Oslo 2021 = 53:55
MLyM3PPhjpE = 1 year ago = From AI first, to user first - Klara Vatn - NDC Oslo 2021 = 58:18
6bkZeR0ptqc = 1 year ago = Reliable Client Server Data Transport for F# web applications - Zaid Ajaj - NDC Oslo 2021 = 52:48
mB9fbotIqe4 = 1 year ago = Building a Gameboy Emulator - David Whitney - NDC Oslo 2021 = 48:41
K8isgioeMf4 = 1 year ago = SOLID Revisited : The State of the Matter - Phil Nash - NDC Oslo 2021 = 50:58
R_VGsI8nFZY = 1 year ago = The Hows and Whys of Running our own OpenID Connect Identity Provider - Roland Guijt - NDC Oslo 2021 = 47:42
qV7D9cV9L7I = 1 year ago = Transitioning to  NET MAUI - Mitchel Sellers - NDC Oslo 2021 = 51:30
Ih5r5qD7bTo = 1 year ago = SAFE Stack: The Pit of Success for Functional Web Programming - Isaac Abraham - NDC Oslo 2021 = 1:02:46
ICBExIB0z-A = 1 year ago = How to really work together as a team - Stacy Cashmore - NDC Oslo 2021 = 52:43
VfPDwxQ3a0U = 1 year ago = Architectural Thinking on Flutter State Management - Majid Hajian - NDC Oslo 2021 = 45:15
4Ohg0b19eng = 1 year ago = Event driven applications in Azure - Laurent Bugnion - NDC Oslo 2021 = 1:01:14
nQA48vH2CCc = 1 year ago = Component Driven Repo for a Component Driven World - Debbie O'Brien - NDC Oslo 2021 = 57:23
k_tavcIrrss = 1 year ago = Debugging one layer deeper - Kevin Gosse - NDC Oslo 2021 = 58:00
mg70_BesZ1Y = 1 year ago = Lending Privilege - Anjuan Simmons - NDC Oslo 2021 = 54:34
lY4chkIR65o = 1 year ago = Good Fences Make Good Neighbors - Trond Hjorteland - NDC Oslo 2021 = 59:00
ddbl2sscPkc = 1 year ago = Working with GraphQL services from F# - Zaid Ajaj - NDC Oslo 2021 = 52:57
K6HVxpcLUoE = 1 year ago = Top Security Threats to Mobile Devices in 2021 & Beyond - Ruby Jane Cabagnot - NDC Oslo 2021 = 14:12
xLjSFXYWdFU = 1 year ago = Stop Punching Yourself in the Face - Hannes Lowette - NDC Oslo 2021 = 50:00
wg0MPgq1eRI = 1 year ago = ASP NET Core Beyond the Introductino - Chirs Klug - NDC Oslo 2021 = 1:01:35
XAKeGAEAJlo = 1 year ago = Time Traveling in the Cloud - Sam Vanhoutte - NDC Oslo 2021 = 1:02:48
DxmipgGhTbA = 1 year ago = No more conflicts: Jamstack that works for developers & business users with Gatsby.js-Arisa Fukuzaki = 55:11
iuy2tbj2kiU = 1 year ago = Make UI tests part of your pipeline - Lars Alexander Jakobsen - NDC Oslo 2021 = 13:03
_lmpAsy1RQ4 = 1 year ago = Writing a MMORPG game in Elm on both client and server - Martin Janiczek - NDC Oslo 2021 = 53:31
13docRUX-Nw = 1 year ago = Why you should consider WebAssembly in your next frontend project - Håkan Silfvernagel = 44:29
DiszmjHEI_Y = 1 year ago = Critical Decision Making - Clifford Aguis - NDC Oslo 2021 = 1:01:46
l8dFcHHo6gc = 1 year ago = Embracing Collaborative Chaos - Lyndsay Prewer - NDC Oslo 2021 = 45:53
5LTT8OfcnsM = 1 year ago = Debugging  NET Apps - Tess Ferrandez - NDC Oslo 2021 = 53:26
a_LM3FJozr0 = 1 year ago = The Next Decade of Software Development - Richard Campbell - NDC Oslo 2021 = 58:20
2DB7qr9saOc = 1 year ago = Microservices for building an IDE - Maarten Balliauw - NDC Oslo 2021 = 50:00
289amg3PYk8 = 1 year ago = Hyper Speed: When Big Data Blooms - Scott Helme - NDC Oslo 2021 = 1:00:29
g-cV156s4wI = 1 year ago = Space in the 2020's - Richard Campbell - NDC Oslo 2021 = 57:25
_cIVa-RctcA = 1 year ago = Automate Yourself Out of a Job with Roslyn - Mark Rendle - NDC Oslo 2021 = 1:00:16
oCFrtZbnN94 = 1 year ago = Developing microservice applications with Dapr - Jakob Ehn - NDC Oslo 2021 = 56:51
Rn8psTi8FBk = 1 year ago = Blazor,  NET 6, and WebAssembly - Steven Sanderson - NDC Oslo 2021 = 59:59
fOsNZDg7GGk = 1 year ago = Passwords are so 1990 - Sam Bellen - NDC Oslo 2021 = 46:46
Djt0LGNMUik = 1 year ago = Demonstrating Binary Exploitation - Marit Iren & Christian Resell - NDC Oslo 2021 = 1:00:21
-AjxMmNAHic = 1 year ago = Implementing an Event Sourcing strategy on Azure - Olena Borzenko & Eldert Grootenboer = 55:58
nvVmFqmZX9s = 1 year ago = The sceptics guide to pattern matching - Matt Ellis - NDC Oslo 2021 = 1:02:04
TmYPhk-jHNc = 1 year ago = When you think there is no time for learning or coding - Eleftheria Batsou - NDC Oslo 2021 = 42:17
91cKQ9MYtaE = 1 year ago = Impactful Mentorship - Eldert Grootenboer & Olena Borzenko - NDC Oslo 2021 = 1:02:11
Hpz6h3izPgY = 1 year ago = Using Immutable Data Structures - Spencer Schneidenbach - NDC Oslo 2021 = 55:10
zKeLSXQVDo8 = 1 year ago = Data Modeling and Partitioning in Azure Cosmos DB - Mark Brown - NDC Oslo 2021 = 1:03:01
qIdr8o37NTo = 1 year ago = Decision Making in the Abscence of Ground Truth - Gary Short - NDC Oslo 2021 = 56:14
OJfcNw9e9cM = 1 year ago = Auditing Data and Answering the life long question Is it the end of the day yet? - Simona Meriam = 36:33
EYU7XriZ24s = 1 year ago = Building a Mobile Flight Simulator - Clifford Agius - NDC Oslo 2021 = 1:01:02
is2hglY6rK8 = 1 year ago = The Leader's Leap - Martin Mazur - NDC Oslo 2021 = 58:00
pvkwzFNwVsc = 1 year ago = An AI with an Agenda - Arthur Dohler - NDC Oslo 2021 = 48:50
qPAWAH3fkro = 1 year ago = Kotlin: Boring Languages are dead  Long Live Boring Languages - August Lilleaas - NDC Oslo 2021 = 43:24
f1yKot6FkaI = 1 year ago = Zero to Document Hero - Luce Carter - NDC Oslo 2021 = 1:01:40
_mZBa3sqTrI = 1 year ago = Plain Text - Dylan Beattie - NDC Oslo 2021 = 54:13
ddwQZtVtVnw = 1 year ago = Introduction to Distributed Systems with C# and .NET at NDC London 2022 = 1:05
R7r3nZTb9V8 = 1 year ago = Hack Yourself First at NDC London 2022 = 0:47
BsUVYk7wQ_g = 1 year ago = Build Automation Revolution - Matthias Koch - NDC Oslo 2021 = 57:36
xBw90a3e_Os = 1 year ago = Learning in Public:: Live Coding on Twitch - Layla Porter - NDC Oslo 2021 = 1:02:58
gvMd45orRXo = 1 year ago = Meet Mark Rendle at NDC London 2022 = 0:30
IyuRQdYHEyA = 1 year ago = Kubernetes isn't the answer - Joe Piscaer - NDC Oslo 2021 = 51:59
gEVp8hLVo_Y = 1 year ago = Enrich your projects with LowCode magic - Rui Santos - NDC Oslo 2021 = 15:15
4Z8nACE9uMg = 1 year ago = Leveraging Stream API within Service Worker - Majid Hajian - NDC Oslo 2021 = 12:58
TENp6xaSd3M = 1 year ago = Desired State How React, Kubernetes and control Theory have lots in common - Branislav Jenco = 45:55
xCeutzpRlzA = 1 year ago = Web Components An Introduction to the Future - Tobias Ljungstrom = 43:51
05Q837IX6M0 = 1 year ago = Drinking a river of IoT data with Akka NET - Hannes Lowette - NDC Oslo 2021 = 1:01:06
WG4Pp1NGXUw = 1 year ago = Building a classic adventure game with Blazor - Sander Molenkamp - NDC Oslo 2021 = 1:00:47
OjBB7_jdm5w = 1 year ago = Managing Asynchronous APIs - Ian Cooper - NDC Oslo 2021 = 57:18
ovD9T-dz9f4 = 1 year ago = From Gin & Tonics at 4 to delivery at pace - Anthony Nicls & Marcel Britsch - NDC Oslo 2021 = 39:12
HYt8tEbR9uk = 1 year ago = Power of Civic Tech Community - Matěj 'Horm' Horák - NDC Oslo 2021 = 7:30
K2AgkMxY6BY = 1 year ago = The Spirit of Creativity - Stephen Haunts - NDC Oslo 2021 = 44:19
dxSpoQ8c7lw = 1 year ago = The Path of Freedom - Stephen Haunts - NDC Oslo 2021 = 1:00:58
F-wEuoJMvls = 1 year ago = NDC Copenhagen Workshop: Introduction to Distributed Systems with C# and .NET - Dylan Beattie = 1:05
xfcOidIqBh8 = 1 year ago = Tomas Jansson - Self service infrastructure using pulumi automation - NDC Oslo 2021 = 57:33
71N4_2Fv3I4 = 1 year ago = Performance Testing  From Zero to Hero with K6 & Azure - Jose Luis Latorre Millas - NDC Oslo 2021 = 54:46
YYtWTXlPTa0 = 1 year ago = Nerd sniping myself into a rabbit hole - Maarten Balliauw - NDC Oslo 2021 = 14:33
-F9VgOrXbOE = 1 year ago = Flying Blind   Lessons Learned from Presenting Online - Alexander Arvidsson - NDC Oslo 2021 = 53:13
MzNQG5Lw2uQ = 1 year ago = NDC Porto Workshop - Introduction to Distributed Systems with C# and .NET - Dylan Beattie = 1:05
kKkQpWk0pV4 = 1 year ago = NDC Security Workshop - Hack Yourself First: How to go on the Cyber-Offence - Scott Helme = 0:47
kO9fenmJ9bA = 1 year ago = APIs for Infrastructure… on steroids - Paul Stack - NDC Oslo 2021 = 56:53
YDTgmcJGbx0 = 1 year ago = Rust wasm: Browser games! - Thomas Heartman - NDC Oslo 2021 = 52:30
R9Ob5Vp4a9c = 1 year ago = Formatting F# Code, There and Back Again - Florian Verdonck - NDC Oslo 2021 = 1:03:01
YPYks7lBKSY = 1 year ago = Computational Creativity - Dylan Beattie - NDC Oslo 2021 = 58:56
WvVrhNMy7DQ = 1 year ago = GitHub Actions DevOps Pipelines as code using C# - Mattias Karlsson - NDC Oslo 2021 = 48:28
BT18uZLTHx8 = 1 year ago = The Perils and Promise of Artificial Intelligence - Richard Campbell - NDC Oslo 2021 = 48:23
4j7PyYT2GMU = 1 year ago = Eventuous  Event Sourcing with  NET - Alexey Zimarev - NDC Oslo 2021 = 57:06
MXKM5dSk_8o = 1 year ago = What's New in F# 6 0  - Don Syme - NDC Oslo 2021 = 59:10
iUFnLbsEAWU = 1 year ago = HelseID Introducing Modern Web Security in a Geriatric Health Sector- Rune Grimstad & Dag Østerhagen = 59:43
h4V6V0u__8I = 1 year ago = The Boeing 737 MAX  When Humans and Technology Don't Mix - Kyle Kotowick - NDC Oslo 2021 = 56:43
qJ5aXkhUzv4 = 1 year ago = Going real time using Azure CosmosDB and React - Olena Borzenko - NDC Oslo 2021 = 44:05
lJCfPhnFLQs = 1 year ago = Roslyn Source Generators   Never send a human to do a machine's job - Stefan Pölz - NDC Oslo 2021 = 1:01:37
ggdBPW_DWbE = 1 year ago = Carving Microservices out of the Monolith with Domain Storytelling -  Henning Schwentner = 52:16
pz4bNmlss3w = 1 year ago = OpenTelemetry will save your day and night - Alexey Zimarev - NDC Oslo 2021 = 59:29
Vt1iS5q1uzk = 1 year ago = How Kubernetes plays Tetris with your containers - Salman Iqbal - NDC Oslo 2021 = 58:24
FtegloxD5nM = 1 year ago = Uno Platfrom  Your apps everywhere - Martin Zikmund - NDC Oslo 2021 = 48:00
ZJw44zIXcE8 = 1 year ago = A Guide To Functional Programming - Jemima Abu - NDC Oslo 2021 = 36:41
9V_ENgl_wVY = 1 year ago = Aligning Bounded Contexts with Subdomains in Legacy Code - Mufrid Krilic. -NDC Oslo 2021 = 55:43
4cKIKvHpSiw = 1 year ago = A continuous fairytale - Oda Hoem & Tina Christin Siversen - NDC Oslo 2021 = 57:29
ou7rNmnVBXY = 1 year ago = Building Cloud Native  NET Applications with Project Tye - Jon Galloway - NDC Oslo 2021 = 1:04:48
TK2WA7CG8VE = 1 year ago = Exploring the Wonderful World of Python on Devices - Brandon Satrom - NDC Oslo 2021 = 42:57
tspbnQB3hvA = 1 year ago = Reactive Programming Crash Course for Angular Baes - Jennifer Wadella - NDC Oslo 2021 = 59:40
kZXiJdmmIKc = 1 year ago = How To Make Your Website A Progressive Web App And Why You Might Want To - Lemon 🍋  - NDC Oslo 2021 = 58:13
vI1gPGjkm7A = 1 year ago = Autonomy, is that what we really want? - Kenny Baas Schwegler & Evelyn Van Kelle - NDC Oslo 2021 = 49:29
dfgsGOW32ns = 1 year ago = Building desktop apps using  NET MAUI and Blazor - Daniel Hindrikes - NDC Oslo 2021 = 30:56
2RiXiyowhWY = 1 year ago = Desktop development in .NET 6 - Olia Gavrysh - NDC Oslo 2021 = 53:00
UBFx3MSu1Rc = 1 year ago = Using the BFF pattern to secure SPA and Blazor Applications  - Dominick Baier - NDC Oslo 2021 = 1:02:16
y2Psj8ACZyw = 1 year ago = OAuth – the good Parts - Dominick Baier - NDC Oslo 2021 = 54:16
qhrd3vq5jkY = 1 year ago = Eliminating Hidden Dangers to Your Applications  Patterns for Reliable Systems - Barry Stahl = 57:43
lL9Ji0wjWMA = 1 year ago = What's new in C#? Exciting new features in C# 8 0 and 9 0 - Filip Ekberg - NDC Oslo 2021 = 1:02:06
C199S4R7cy8 = 1 year ago = Developer Fundamentals of Serverless NET Development with Azure Durable Functions - Jonah Andersson = 54:14
Z1_D0GJ7CB4 = 1 year ago = Choreography vs Orchestration in serverless microservices - Mete Atamel & Guillaume Laforge = 1:02:30
y7nJ3eWAQ3o = 1 year ago = Does spam have an opinion? Using machine learning to understand your spam - Lars Klint - NDC Sydney = 1:13:40
u5ub-KP_2N4 = 1 year ago = How to Become a Tech Conference Speaker - Brooke Jamieson - NDC Sydney 2021 = 1:00:26
4N-5iL_FBUU = 1 year ago = Flexing your Biceps with Azure - William Liebenberg - NDC Syndey 2021 = 54:39
iSWxny5MUY8 = 1 year ago = Common mistakes in EF Core  - Jernej Kavka - NDC Sydney 2021 = 53:33
EY_8euvtLnk = 1 year ago = Type-safe GraphQL with TypeScript - Aaron Powell - NDC Sydney 2021 = 1:00:09
Ye8Pks1_IJ4 = 1 year ago = Leadership Through Self Awareness - Melissa Houghton - NDC Sydney 2021 = 55:39
36MEItqw328 = 1 year ago = Inside a static analyser: type system - Yuri Minaev - NDC TechTown 2021 = 50:23
U1NNgQaC300 = 1 year ago = Delivering code with GitHub Actions - Antonio Liccardi  - NDC TechTown 2021 = 54:14
fVzk4JY2w-M = 1 year ago = Secure Coding in C and C++  - Volatility Ahead - Robert Seacord - NDC TechTown 2021 = 47:01
NS87tWsbyPQ = 1 year ago = Little Red Riding Hood & the k-d tree forest - Jørgen Kvalsvik - NDC TechTown 2021 = 50:37
oQbBSOs1EHw = 1 year ago = TestOps at scale - James Westfall - NDC TechTown 2021 = 56:25
Clr_MQwaJtA = 1 year ago = Diving deeper into control groups (cgroups) v2 - Michael Kerrisk - NDC TechTown 2021 = 1:01:50
kcnFQgg9ToY = 1 year ago = An introduction to control groups (cgroups) version 2 - Michael Kerrisk - NDC TechTown 2021 = 56:57
uKDXwKe0fyo = 1 year ago = Catching up with Catch2: Changes recent and future - Martin Hořeňovský - NDC TechTown 2021 = 49:07
KVM5njlZ4sM = 1 year ago = An Introduction to Android Automotive OS - Chris Simmonds - NDC TechTown 2021 = 48:11
z-zPTWp6xbY = 1 year ago = TypeScript for C++ programmers - Ólafur Waage - NDC TechTown 2021 = 50:10
XAL4GlBt_Yk = 1 year ago = A (short) Tour of C++ Modules - Daniela Engert - NDC TechTown 2021 = 1:01:05
1u6DdiFFH6Q = 1 year ago = Keynote: Testing as an equal 1st class citizen (to coding) - Jon Jagger - NDC TechTown 2021 = 58:17
KfYkkQJF_wk = 1 year ago = Introducing a matrix class to the C++ standard library - Guy Davidson - NDC TechTown 2021 = 59:47
nudq58d0TFc = 1 year ago = A Physical Units Library For C++ - Mateusz Pusz - NDC TechTown 2021 = 1:01:56
Ko0eV7BGcXs = 1 year ago = SOLID Revisited : The State of the Matter - Phil Nash - NDC TechTown 2021 = 1:00:24
HalN3dTUnL8 = 1 year ago = Implementing C++ Semantics in Python - Tamir Bahar - NDC TechTown 2021 = 51:27
uyaYBD8-xq0 = 1 year ago = Real Programming - Sjur Julin - NDC TechTown 2021 = 29:01
PD-Q0nhkegM = 1 year ago = Demonstrating binary exploitation  - Marit Iren Rognli Tokle & Christian Resell = 58:04
v0ssX-JiV-s = 1 year ago = The Genius of the RISC-V Microprocessor - Erik Engheim - NDC TechTown 2021 = 1:00:36
s5U4c2_ChrA = 1 year ago = How to write a really good board support package for Yocto Project - Chris Simmonds = 58:27
BUUWEkpGWsM = 1 year ago = Software Engineering Is About Tradeoffs - Mateusz Pusz - NDC TechTown 2021 = 58:34
AzQQPyBwNyo = 1 year ago = Agile embedded development under regulatory constraints - Espen Albrektsen - NDC TechTown 2021 = 1:04:50
bUZ_tTy7Seo = 1 year ago = Virtual Reality with Qt Quick 3D - Andy Nichols - NDC TechTown 2021 = 35:36
B6LSdboN_wM = 1 year ago = Designing a modern build system and dependency manager, how hard can it be? - Jussi Pakkanen = 41:01
_RXU-hAS87U = 1 year ago = What has writing about the Core Guidelines shown me? - Guy Davidson = 1:07:35
6AIYIf5Vr18 = 1 year ago = How to start using coroutines - Mikhail Svetkin - NDC TechTown 2021 = 46:56
uPJFj3b8RN0 = 1 year ago = Asynchronous I/O and coroutines for smooth data streaming - Björn  Fahller - NDC TechTown 2021 = 57:10
9mPEdpUNZfc = 1 year ago = Dependency Management in C++ - Patricia Aas - NDC TechTown 2021 = 1:04:19
HB_wfa1F31o = 1 year ago = Instrumenting machine code over WebRTC - Ole André Vadla Ravnås - NDC TechTown 2021 = 1:00:52
fGnbGX88z3Y = 1 year ago = From Program to Process - What Happens After the Compiler - Anders Schau Knatten - NDC TechTown 2021 = 59:57
SxK-hccyoTc = 1 year ago = Sandboxing a Linux application - Martin Ertsås - NDC TechTown 2021 = 41:43
rq4_31OkdWA = 1 year ago = NDC Oslo 2021 | Live in Oslo Spektrum = 0:33
yYCh7OTmbD0 = 1 year ago = NDC TechTown 2021 | Conference for Embedded Development = 1:10
d5DjKtPUrcc = 1 year ago = Introduction to Distributed Systems with C# and .NET with Dylan Beattie at NDC Oslo 2021 = 2:01
OAwUu2b0F_U = 1 year ago = Wait, I have to test the front end too? - Amy Kapernick = 53:22
dR9V53nQnsw = 1 year ago = FaaS or not to FaaS? Visible and invisible benefits of the Serverless paradigma - Vadym Kazulkin = 51:20
3tzsn9rwC7s = 1 year ago = Creating a hybrid and multi-cloud strategy using Azure API Management = 1:03:00
4ZfJG2RB0_E = 1 year ago = Let systems communicate using Azure Integration Services - Steef-Jan Wiggers - NDC Sydney 2020 = 45:10
8lmrDYrvo8g = 1 year ago = Multi-cloud portability for Go applications - Praveen Yedidi - NDC Sydney 2020 = 37:01
C1FW0-BRbEs = 1 year ago = A Deep Dive Into SameSite Cookies, What They Are and Why They Matter - Stephen Rees-Carter = 42:25
DNA2t0_R84A = 1 year ago = Taking Models to the Next Level with Azure Machine Learning - Henk Boelman - NDC Sydney 2020 = 56:54
DV9cifABfdo = 1 year ago = JavaScript for emails, are you sure? - Phil Nash - NDC Sydney 2020 = 59:07
EcyLVccRGMo = 1 year ago = Deploying Docker for Database DevOps Dominance - Daniel Mallott - NDC Sydney 2020 = 56:26
FO0YdgSUCHo = 1 year ago = Goodbye Regex. Hello Parsers! - Hackle Wayne - NDC Sydney 2020 = 58:20
LScwAIatCuI = 1 year ago = Say YES! to NoSQL: A Guide on When to Ditch Relational Databases - Adrienne Tacke - NDC Sydney 2020 = 44:49
LZ0Zku-a464 = 1 year ago = Tips and tricks for robust big data applications - Yousry Mohamed - NDC Sydney 2020 = 53:12
Om3sesUa3GE = 1 year ago = Event-driven serverless architectures using Knative and Cloud Run - Mete Atamel - NDC Sydney 2020 = 54:51
SmIzXpPEiA0 = 1 year ago = Unleash the Power of VS Code - Aaron Powell - NDC Sydney 2020 = 57:12
Sru_L6ldskQ = 1 year ago = CI/CD and beyond with GitHub Actions - Damien Brady - NDC Sydney 2020 = 59:46
U2zEKLxcArg = 1 year ago = From bulb to C# — how does computer work? - Adam Furmanek - NDC Sydney 2020 = 1:02:47
Wcj-ueRrWg8 = 1 year ago = Cache Me Outside - Caching Methodologies & Architectures - Anthony Dang - NDC Sydney 2020 = 42:59
YF6BxSSH35w = 1 year ago = Modernizing a legacy app using Windows Containers and Kubernetes: Challenges and Lessons learned = 16:21
ZCHzTG8fCuY = 1 year ago = State of WebXR: What do You Need to Know Today? - Rabimba Karanjai - NDC Sydney 2020 = 26:46
fYCfB7MZPh4 = 1 year ago = The Rise of Software Supply-Chain Attacks – How Secure is your .NET Application? - Niels Tanis = 57:19
fzvPqeUP_KI = 1 year ago = Using GraphQL as a Secure Innovation Boundary and data-driven culture driver -  Rob Moore = 1:00:04
hI63fHhjmeQ = 1 year ago = Handling secrets in cloud-based applications - Steve Roberts - NDC Sydney 2020 = 55:11
hV43fiHYBb4 = 1 year ago = Clean Testing: Clean Architecture with .NET Core - Jason Taylor - NDC Sydney 2020 = 46:11
iXt69OeEtXE = 1 year ago = Unit Testing Deconstructed - Emily Taylor - NDC Sydney 2020 = 20:58
jKgctC0fWUE = 1 year ago = Building Qrio, a Bot That Plays Videos for My Toddler - Agustinus Nalwan - NDC Sydney 2020 = 42:48
rm1QSXhSP3k = 1 year ago = Vue.js is going to take the world - Thiago Passos - NDC Sydney 2020 = 1:03:00
wCfVHaGzb74 = 1 year ago = Fighting Back Against a Distracted World - Increasing your Focus and Self-motivation -Stephen Haunts = 1:04:55
y_f7ZrLQi9w = 1 year ago = Flexibility with Serverless Azure Functions - Nelly Sattari - NDC Sydney 2020 = 16:06
yqWJcXlHw1I = 1 year ago = Practical Applications of ML in Software Testing - Mesut Durukal - NDC Sydney 2020 = 50:25
iT4Ooqze9nk = 1 year ago = The Agenda is out - NDC Oslo 2021 = 1:38
AbVZz509E9A = 1 year ago = 15 Minute Yoga for Software Developers - Amy Dunstan - NDC Melbourne 2021 = 14:20
hX1srCWtDsc = 1 year ago = Power BI Embedded Analytics Explained - Peter Myers - NDC Melbourne 2021 = 44:27
_EjuTp81SYQ = 1 year ago = 4 Steps from JavaScript to TypeScript  - Phil Nash - NDC Melbourne 2021 = 40:05
K-fSli9S5kM = 1 year ago = Machine Learning for Software Developers (...and Knitters) - Kris Howard - NDC Melbourne 2021 = 55:39
nnuLeQNfruA = 1 year ago = Introduction to Digital Twins with the Azure Digital Twin Platform - Alex Mackey - NDC Melbourne = 45:09
gvyTB4aMI4o = 1 year ago = Functional Programming with C# - Simon Painter - NDC Oslo 2020 = 1:03:21
XjFgjBavPmI = 1 year ago = GitHub Like a Boss - Michelle Mannering - NDC Melbourne 2021 = 48:08
lxwNcg2q1-Y = 1 year ago = Records Deep Dive: What, Why and How - David Wengier - NDC Melbourne 2021 = 43:57
vjx0lIMamZs = 1 year ago = Scott Hanselman - Beyond Mentorship - Storytelling and Sponsorship - NDC Melbourne 2021 = 1:06:14
16Nex5MDbW0 = 1 year ago = How to develop to be compliant with OAuth 2.1 out of the gate - Nahid Farrokhi - NDC London 2021 = 49:47
1V-Htcc3fW0 = 2 years ago = DRY TDD with AutoFixture - Enrico Campidoglio = 53:45
sZsG1Ry78ww = 2 years ago = Incidents are a new normal - Kasia Szulc - NDC London 2021 = 37:17
VDGk0fweHcg = 2 years ago = Intro to Blazing Web Accessibility  - Empowered with AI - Dennie Declercq = 57:03
hIQa7SsWYUE = 2 years ago = The top 10 best new features in C# version 6 to 9 - Chris Klug = 1:05:57
dmuVLR_XbsI = 2 years ago = Breaking the language barrier: how do we quickly add multilanguage support in our AI application? = 43:04
UV4GhPY7BB0 = 2 years ago = Ten Things Every Voice Application Should Do - Jeff Blankenburg - NDC London 2021 = 47:34
YHkBmxpCFAg = 2 years ago = A Tour of Go for the C# Developer - Jeremy Clark - NDC London 2021 = 1:00:19
Gdq1H-Fci5Q = 2 years ago = The Implementation and Practice of DevSecOps - Jihai Zhou = 43:53
EnNLvf2THCw = 2 years ago = NodeJS, ML, K8s and Unethical Face Recognition - Joel Lord - NDC London 2021 = 53:04
ly7GuN505UM = 2 years ago = DevOps with Azure Kubernetes Service = 1:01:24
3KKy3qGr-Ic = 2 years ago = ReST API Design: A beginner's guide - Janani Subbiah - NDC London 2021 = 49:39
IqB8nVPCS64 = 2 years ago = Practical Domain-Driven Design with EF Core - Hossam Barakat - NDC London 2021 = 56:29
QA2QdBG5uLE = 2 years ago = Agile Evolution: An Enterprise transformation that shows that you can too - Martin Hinshelwood = 1:00:44
cxWbY_DA2oI = 2 years ago = Why you should consider Web Assembly in your next frontend project - Håkan Silfvernagel = 42:48
lTCh80MCLOY = 2 years ago = Why your company needs an internal API and what you should do about it - Glenn F. Henriksen = 41:24
5VQz28oABo0 = 2 years ago = Asynchronous Distributed Systems - David Ostrovsky - NDC London 2021 = 1:02:12
JAafBEoqENE = 2 years ago = TestCafé: Web Testing Made Easy! - Don Wibier - NDC London 2021 = 48:34
B4RPe4VpEWc = 2 years ago = The Mario Kart™ guide to building a career - Hannes Lowette - NDC London 2021 = 53:03
jt6FBbuKUYY = 2 years ago = Offline web applications don't exist anymore! - Francesco Leardini - NDC London 2021 = 51:33
dCsxVSY-6Dg = 2 years ago = Web Components as micro apps - Craig West - NDC London 2021 = 47:40
hOeKlz4owzY = 2 years ago = The Untruthful Art - Five Ways of Misrepresenting Data - Alexander Arvidsson - NDC London 2021 = 51:08
DyZ-BSIi8Wo = 2 years ago = Retrospectives Antipatterns - Aino Vonge Corry - NDC London 2021 = 59:15
CXO6eeon2rQ = 2 years ago = Orchestrate and build serverless solutions with Azure Logic Apps - Brian Gorman - NDC London 2021 = 54:01
ygFuOs7c-mw = 2 years ago = Service Principals and Managed Identities - the Identity tools every Azure developer should know = 50:44
g06igkxbF78 = 2 years ago = Thirteen ways of looking at a Turtle - Scott Wlaschin - NDC London 2021 = 1:07:04
SZCWKcJ_O2Q = 2 years ago = Unleash the Power of VS Code - Aaron Powell - NDC London 2021 = 59:33
K6oXfgUFNsM = 2 years ago = When to go from collaborative modelling to coding? - Gien Verschatse - Kenny Baas-Schwegler = 54:21
vOO3hulIcsY = 2 years ago = TDD Revisited - Ian Cooper - NDC London 2021 = 1:00:43
ALN1v_sBe2g = 2 years ago = Web Performance Tuning with browser APIs - Yaser Adel Mehraban - NDC London 2021 = 1:02:02
kBQ4Af7g4k8 = 2 years ago = Writing Cross Platform Games with MonoGame and .NET - Stephen Haunts - NDC London 2021 = 42:44
bais_idyk_I = 2 years ago = Power your .NET application with the new generation of diagnostics - Raffaele Rialdi = 55:27
VrZRLbSYZiM = 2 years ago = How to secure your GitHub Actions - Rob Bos = 51:03
7pONldOAxws = 2 years ago = Getting Started with Computer Vision - Seth Juarez - NDC London 2021 = 1:00:32
nHxnDOTmROY = 2 years ago = Gaining Confidence with Cypress Tests - Rob Richardson - NDC London 2021 = 57:14
NtEtV5Jc2ac = 2 years ago = I know what you did last project (common mistakes we make in Azure) - Sasha Kranjac, Mustafa Toroman = 57:36
RzyLfDqsgSo = 2 years ago = Finding System Boundaries with Domain Storytelling - Stefan Hofer - NDC London 2021 = 38:58
JwVtscL9H9k = 2 years ago = .NET Core Dependency Injection – The Booster Jab - Steve Collins - NDC London 2021 = 54:55
o-HNxQ25pfg = 2 years ago = Designing composable functional libraries, not just for data visualization - Tomas Petricek = 48:28
ksCTuK68TXA = 2 years ago = Securing Multitenant Databases with Entity Framework Core - Zoran Horvat - NDC London 2021 = 1:00:21
g7iZ3ODmIUs = 2 years ago = Little Fluffy Clouds - Liam Westley - NDC London 2021 = 56:21
9IVJ2ts0zQo = 2 years ago = Mobius – writing your own .NET runtime running on .NET Core - Konrad Kokosa - NDC London 2021 = 58:16
evNRI7h_4Zk = 2 years ago = Authentication and Authorization in Blazor - Marco De Sanctis - NDC London 2021 = 56:47
yiNHhaX-adY = 2 years ago = The Rise of Software Supply-Chain Attacks – How Secure is your .NET Application? - Niels Tanis = 58:29
RY7cb-BQO8Q = 2 years ago = Building a Robot Arm with .NET 5, Raspberry Pi, Blazor and Signal R - Peter Gallagher = 56:24
E8NaMb8rx1k = 2 years ago = Automating Android: Command line controls - Quintin Balsdon - NDC London 2021 = 56:59
xGo6XUn0WQg = 2 years ago = Advanced Bluetooth® Technology - Under the APIs - Martin Woolley - NDC London 2021 = 57:50
iUXQ40rn0ig = 2 years ago = Access All Areas: Making Accessibility More Accessible - André Lemos  -NDC London 2021 = 53:14
QYWoHuV78Oo = 2 years ago = Running PHP apps on .NET 5 - Jakub Míšek & Ben Fistein - NDC London 2021 = 55:43
1nP7hEvAMiw = 2 years ago = Software and Database Refactor Patterns - Bill Penberthy - NDC London 2021 = 50:20
Uc7xkLZFcW8 = 2 years ago = A pragmatic approach to turn your data into actionable insights - Irina Dragunova - NDC London 2021 = 58:59
aeNFTdEKuEk = 2 years ago = Lessons Learned from the Trenches: Connectivity and Performance Tips&Tricks, Jose Manuel Jurado Diaz = 59:08
rEKV7ZSRueE = 2 years ago = REST - The ignored parts - Irina Scurtu - NDC London 2021 = 1:00:57
P-Ke4vK1d38 = 2 years ago = Dude, where is my class?! - Hackle Wayne - NDC London 2021 = 58:14
r82WJQIHL0Y = 2 years ago = The leadership balancing act - achieving success without burning out - Donna Edwards = 55:09
t0lT8eRPyuc = 2 years ago = Evolutionary history of the RabbitMQ .NET Client towards concurrency - Daniel Marbach = 59:54
w_ZLEuo6zl4 = 2 years ago = DevOps for Your Relational Database Foundations - Brian Randell - NDC London 2021 = 59:45
Vpc1uxJi37E = 2 years ago = CI/CD and beyond with GitHub Actions - Damian Brady - NDC London 2021 = 56:03
szb1MG-lrHM = 2 years ago = Building a Mobile Flight Simulator - Clifford Agius - NDC London 2021 = 50:42
beZIwiTi_Ik = 2 years ago = How To Make Your Website A Progressive Web App (And Why You Might Want To) - Lemon 🍋 = 35:46
S8ibDpdo5BE = 2 years ago = Infrastructure *is* Code with the AWS Cloud Development Kit - Steve Roberts - NDC London 2021 = 53:00
_ncO6kUP-zs = 2 years ago = Hot Chocolate: GraphQL Schema Stitching with ASP.Net Core - Michael Staib - NDC London 2021 = 52:12
biT5-mQ2ekc = 2 years ago = Postponing architectural choices and start developing first with Dapr - Michaël Hompus = 1:02:42
ePNfQ-rj0VQ = 2 years ago = Microsoft Q# and Azure Quantum - Johnny Hooyberghs - NDC London 2021 = 1:03:18
aI4hi4xKYtE = 2 years ago = Hiding The Lead - Sam Newman - NDC London 2021 = 52:57
Mcu9Gm4wPf8 = 2 years ago = OpenTelemetry 101 - Rob Ashton - NDC London 2021 = 57:57
r_tl0UAbNQ8 = 2 years ago = Getting Started with GitHub Actions - Mickey Gousset - NDC London 2021 = 1:00:34
dtZB2fqZuG0 = 2 years ago = Observable Web Applications - Todd Gardner - NDC London 2021 = 52:43
7MWXTXjtl8s = 2 years ago = HTTP Security Headers You Need To Have On Your Web Apps - Scott Sauber - NDC London 2021 = 59:22
FMEQVOmEpck = 2 years ago = 🤖  Building a Telegram bot with Apache Kafka and ksqlDB - Robin Moffatt - NDC London 2021 = 59:20
XMwoqc0aayA = 2 years ago = When Open Source Came to Microsoft - Richard Campbell - NDC London 2021 = 54:21
iLdgJB3ZC1k = 2 years ago = Blazor, GraphQL and a headless CMS - Poornima Nayar - NDC London 2021 = 56:07
LOzMldQ5cw8 = 2 years ago = Smart home from scratch - a little C#, a little C++ and a whole lot of cheap Chinese electronics = 49:50
kRI5geKohjo = 2 years ago = OAuth in 2021 – What’s up? - Dominick Baier - NDC London 2021 = 1:02:23
pP4lumdqpXY = 2 years ago = Building a Game Boy emulator in .NET Core! - David Whitney - NDC London 2021 = 51:16
t2AMDthNSl8 = 2 years ago = Blazor & gRPC - Code-first .NET SPA developer productivity - Christian Weyer - NDC London 2021 = 1:03:07
sFY-vrZmHow = 2 years ago = Getting Started with Unity and AR/VR for the .NET Developer - Davide Zordan = 56:37
fj5RB958M_4 = 2 years ago = The Ultimate Guide To Building Better Azure ARM Templates - Eldert Grootenboer - NDC London 2021 = 1:02:07
JFbnPoXMpqQ = 2 years ago = Reactive Programming, State Management, and Redux for the Modern Front End Dev - Jennifer Wadella = 1:00:14
xZ0_NwxDJxc = 2 years ago = Migrate your Web Apps to ASP.NET Core, one page at a time - Mark Rendle - NDC London 2021 = 57:07
l-SCY3Hetg4 = 2 years ago = JavaScript for emails, are you sure? - Phil Nash = 59:16
YUEvsk9TzmM = 2 years ago = Managing the Burnout Burndown - Anjuan Simmons = 59:41
ILC0RP-NcLE = 2 years ago = The Dark Side Of Events - Vladik Khononov = 54:14
lrob86feodY = 2 years ago = Battles of an Impostor - Melissa Houghton = 47:14
0H68V2BzutA = 2 years ago = From a distributed monolith to a microservices solution - Jan de Vries = 54:12
x7oYYLgZgtY = 2 years ago = Hot Chocolate: An introduction to GraphQL on ASP.Net Core - Michael Staib = 1:04:02
VxwPJxqmZUk = 2 years ago = The Mario Kart™ guide to career planning -  Hannes Lowette = 57:15
1lMYyoPl2Qk = 2 years ago = Elephant in the room and Innovation! - Nelly Satari = 23:27
vpop0OIPyrE = 2 years ago = Nerd sniping myself into a rabbit hole. Streaming online audio to a Sonos speaker - Maarten Balliauw = 50:28
zh6nrL-fGfg = 2 years ago = Event Sourcing with EventStore and Go - Ken Faulkner = 16:17
3Ll9t15FW6g = 2 years ago = Machine Learning simplified for Developers with ML.NET - Jernej Kavka = 59:09
KHAlHqS0c-g = 2 years ago = Demystifying Front-End Security - Ilya Verbitskiy = 52:05
vQrnVD6CbxU = 2 years ago = Kill All Mutants! (Intro to Mutation Testing) - Dave Aronson = 52:16
4oSDZI4oiAw = 2 years ago = Not all “Microservices frameworks” are made the same - Dasith Wijesiriwardena = 16:55
sh73B_3ZLVc = 2 years ago = IoT Solution Recipes - Beyond your first slice of Raspberry Pi - Adam Stephensen & Valeriia Savenko = 55:26
WK7W3xHmVbU = 2 years ago = NDC Manchester - 25 March 2021 - Live and Online = 1:33
ZVHahxlp8QI = 2 years ago = Creating a hybrid and multi-cloud strategy using Azure API Management - Eldert Grootenboer = 1:03:06
yc0dXM7Sz9s = 2 years ago = The Persuasion Equation - Brooke Jamieson = 46:17
rJC2VXftAWc = 2 years ago = Artificial Intelligence? - more like Artificial Stupidity! - Aiko Klosterman = 55:41
HVs5IISO9yg = 2 years ago = Say YES! to NoSQL: A Guide on When to Ditch Relational Databases - Adrienne Tacke = 44:56
59V0lylQzmE = 2 years ago = Eating an Elephant: Conquering big projects one bite at a time. - Liam Elliott = 47:34
u1WBH8HaI-4 = 2 years ago = Building Rock SOLID Serverless Applications - William Liebenberg = 53:13
qYYgxtCai6o = 2 years ago = Innovation and Trends in Flutter for web - Kamal Shree = 41:46
LiN6Gf3sE8w = 2 years ago = Biometric security in the Azure Cloud - Stefano Tempesta = 59:32
RMpP8XeJ8kY = 2 years ago = Graphing Your Way Through the Cosmos: Common Data Problems Solved with Graphs - Chad Green = 56:45
903-02KFjwQ = 2 years ago = Cloud-Native Kubernetes Workflows on AKS with Argo - Rahul Rai & Tarun Pabbi = 51:50
A0jn_77eRCw = 2 years ago = Ordering the chaos - cleaning logs and ordering events in microservices - Adam Furmanek = 1:01:35
u2H06FG4kBA = 2 years ago = NDC London 25-29 January 2021 - Live and Online = 0:31
9xveNg4zhJA = 2 years ago = Modernizing an existing system to take a more domain-driven approach - William Penberthy = 58:08
-1mffwoCgOI = 2 years ago = A deep dive into Conversational AI with Microsoft Bot Framework - Arafat Tehsin = 1:02:54
1NPhr5UeTqs = 2 years ago = Easier infrastructure and safer secrets with Pulumi, Azure, and .Net Core - Rian Finnegan = 56:13
FR0HzDWBmz0 = 2 years ago = Common mistakes and misconceptions in Web App Security using OAuth 2.0 and OpenId Connect = 1:05:10
9QeSYCFUpzU = 2 years ago = Svelte, cybernetically enhanced web apps - Devlin Duldulao = 53:18
FSOaB4wTlxU = 2 years ago = The Power of Performance Feedback - Amber Vanderburg = 1:00:36
Z-Rh4eB6uA8 = 2 years ago = Cloud-Native Kubernetes Workflows on AKS with Argo - Rahul Rai & Tarun Pabbi = 51:50
y4T9uGkdwHw = 2 years ago = Fixing poor performance patterns in Azure SQL Database applications - Martin Cairney = 58:25
hI6yknJLf-I = 2 years ago = Serverless Azure In The Enterprise - Duncan Hunter & Adam Stephensen = 54:35
AyzVIIGhd-I = 2 years ago = Effective Communication in a Remote First World - Rob Crowley = 55:25
ppblyFtQDvo = 2 years ago = Introduction to PASETO (platform-agnostic security tokens) - Ruby Jane Cabagnot = 10:09
kfyCHtqk-Ts = 2 years ago = Distributed Tracing Made Easy with .NET Core - Jimmy Bogard = 1:02:34
edu_GJ6tI60 = 2 years ago = Make your mouse move like a human - modern AI directly in web browser - Jakub Ledworowski = 12:47
OfDEVJHo-mo = 2 years ago = The sunny side of AI - Henk Boelman = 19:20
X80WADHy8GM = 2 years ago = Securing Serverless Applications in Azure - Sjoukje Zaal = 50:26
oyCcuPKJyxg = 2 years ago = The Background on Background Tasks in .NET Core - Scott Sauber = 58:33
oc6hbOocMa4 = 2 years ago = Common quandaries implementing your first Event Driven Architecture - Sarah & Ann = 45:12
v4R1YB_qo94 = 2 years ago = What We Learned Going Serverless - Illia Kavaliou = 47:27
LWRdqkxV3xw = 2 years ago = PWA For Games: An Enhanced Web Gaming Experience - Stephen Vinuya = 56:29
z3a1Tl-XNtg = 2 years ago = Rise of the Machines – Technology in Humanity - Lars Klint = 46:18
yxtsTEhb140 = 2 years ago = Practical Domain-Driven Design with EF Core - Hossam Barakat = 55:13
AeMuJY1XET4 = 2 years ago = AI for the better - Dennie Declercq = 52:31
pqLs7X6Cr6s = 2 years ago = C# Source Generators - Write code that writes code - David Wengier = 59:14
mHDuXpS7-UY = 2 years ago = Eventing with Knative and Cloud Run: From Basics to Advanced - Mete Atamel = 1:00:04
F-2dqinlH8g = 2 years ago = A Friendly Introduction to Deep Learning for Computer Vision - Seth Juarez = 59:27
JRoZBep6pDo = 2 years ago = Machine Learning for .NET developers - Olia Gavrysh = 56:20
mxvEsF3NYtY = 2 years ago = Kafka as a Platform: the Ecosystem from the Ground Up - Robin Moffatt = 1:00:00
l7qUyL2vzL8 = 2 years ago = Running atomic transactions across multiple data models?!? - Loris Cro = 43:31
ekE7cs3TDFU = 2 years ago = Production readiness in Azure: A practical guide - David Pazdera = 42:18
88ZCRpqZg74 = 2 years ago = Tackling Social-technical complexity in the heart of your team - Evelyn & Kenny = 59:57
olE6PrCD89E = 2 years ago = Vue.js is going to take the world - Thiago Passos = 58:29
6sv7jtWKU1A = 2 years ago = How not to choke on a big old project - Yuri Minaev = 46:51
gWxBonPkrGM = 2 years ago = The Pipes Library: How Plumbing Can Make Your Code More Expressive - Jonathan Boccara = 1:00:23
28wu6sXnTBs = 2 years ago = QProperty - QML property binding in C++ - Mikhail Svetkin = 51:22
mSkVkPG0m80 = 2 years ago = Leadership Guide for the Reluctant Leader - David Neal = 56:52
jrfZDtDgKYk = 2 years ago = What do you mean by "Cache Friendly"? - Björn Fahller = 1:00:35
hqo6bdnwPH8 = 2 years ago = Lazy QObject tree traversal - Vitaly Fanaskov = 38:22
Gpfr4RvRdfk = 2 years ago = Proactive Security, less buzzword, more action - Siren Hofvander = 39:16
0CJMN_kvL5Q = 2 years ago = Paradigms Lost, Paradigms Regained: Programming with Objects and Functions and More - Kevlin Henney = 52:06
tbrZGXtdnYE = 2 years ago = Coroutines are Qt: safer thread pools interactions -  Pietro Fezzardi & Alain Carlucci = 52:06
2T97nULFVb0 = 2 years ago = C++ Parallel Programming Models - Eran Gilad = 50:26
Ybmomkc48wg = 2 years ago = C++ Error Handling Revisited - Raphael Meyer = 57:46
5G3EtDwW4Xs = 2 years ago = C++ ecosystem: the renaissance edition - Anastasiia Kazakova = 58:06
OAQy7ysp93I = 2 years ago = Algorithmic and microarchitecture optimizations of C++ applications -  Alexander Maslennikov = 34:31
pLMKbNQdSoI = 2 years ago = Embracing Simplicity - Guilherme Ferreira = 50:53
wEPYczHSf-w = 2 years ago = Battles of an Impostor - Melissa Houghton = 44:33
7TOakcl5ANQ = 2 years ago = 25 Years of SSL - Secure(ish) Sockets Layer - Scott Helme = 58:29
eYKM_wJNzUY = 2 years ago = Trying to build an Open Source browser in 2020 - Patricia Aas = 58:26
R5cw9Q3BL0E = 2 years ago = Hiding The Lead - Sam Newman = 45:50
4vqTFVEkPPo = 2 years ago = Rise of the Machines – Technology in Humanity - Lars Klint = 50:33
dQ9SpExTi08 = 2 years ago = Advanced OAuth - Private In-House Training with Dominick Baier = 1:57
dubHmScPNzQ = 2 years ago = Navigating microservices with .NET Core - Ryan Nowak = 1:07:24
XLOZ3hhJKBE = 2 years ago = Building real-time applications with Blazor and GraphQL - Michael Staib = 1:00:52
QataQnV42Z4 = 2 years ago = Getting graphy - a hands-on crash course with Neo4j - Ljubica Lazarevic = 1:01:53
4dzpIjyb9mM = 2 years ago = Microservices for building an IDE – The innards of JetBrains Rider - Maarten Balliauw = 58:42
StOGzJz5A9k = 2 years ago = The Ethical Dilemma of AI: Save the World or Forsake It? - Tim Huckaby = 1:02:49
Id5O-doqqIs = 2 years ago = Don't Fly Blind - Implementing Effective Application Instrumentation - John Garland = 59:33
z4RaGeipF0c = 2 years ago = Security Tooling in Your DevOps Pipeline - Nancy Gariché = 38:52
BDJvoIjF1aA = 2 years ago = Keep your nose out of it. Denying yourself access to production - Glenn F. Henriksen = 57:00
r_CoAkk9xRY = 2 years ago = 3D printed Bionic Hand a little IOT and a Xamarin Mobile App - Clifford Agius = 1:03:24
VJv-Jfs0fyk = 2 years ago = Migrate and Modernize with Kubernetes and Windows Containers - Vishwas Lele = 59:00
cNu0lzO-sjk = 2 years ago = Owning Your Experience: Talking about Mental Health In the Workplace - Arthur Doler = 52:51
GbiMcsX9-Y0 = 2 years ago = AI in the battle against fakes - Henk Boelman = 59:23
IEDbFaKONTI = 2 years ago = Rendering 3D Worlds in C# - David Whitney - NDC Oslo 2020 = 59:46
UarhPT1M83M = 2 years ago = How we almost delivered 100 tons of Stracciatella Mousse - Björn Wendland & Tobias Schröder = 46:15
Bj0GQ9HSPLM = 2 years ago = Data Mesh in Practice - Arif Wider & Max Schultze - NDC Oslo = 54:10
SYqGu24UzFs = 2 years ago = From Tables to Documents -- Changing Your Database Mindset - Lauren Schaefer - NDC Oslo 2020 = 46:11
h-MiWjs5yMw = 2 years ago = BeeIoT - Enter the World of Bees - Tom Erik Støwer & Kim Bredesen - NDC Oslo 2020 = 59:47
MpTiXJo6i2g = 2 years ago = It's a Polyglot World - Mark Fussell & Shailendra Singh Chauhan - NDC Oslo 2020 = 57:30
-OfBhk8x_Nw = 2 years ago = OpenFaaS: Serverless platform with no strings attached? - Andreas Mosti - NDC Oslo 2020 = 22:43
1M_OfvqtNJk = 2 years ago = Why we’ll never see time travellers of the 80s in year 2038 - Sindre Lindstad - NDC Oslo 2020 = 11:59
zxa1xHQgEjo = 2 years ago = SQL Server hates you(?) - what the DBAs never told the developers - Alexander Arvidsson - NDC Oslo = 57:25
KSH8-2x5j-U = 2 years ago = Building Quality in Legacy Systems - The Art of Asking Questions - Mufrid Krilic - NDC Oslo 2020 = 12:16
kkyB0Pm9Yew = 2 years ago = Browser Fingerprinting: Stalking With a Personal Touch - Eivind Arvesen - NDC Oslo 2020 = 13:41
OIRSbNxkiKE = 2 years ago = A motivating process for deriving Objectives and Key Results (OKRs) - Helge Grenager Solheim = 10:06
viGBcXZF6dU = 2 years ago = Azure cloud for the web frontend developers - Maxim Salnikov - NDC Oslo 2020 = 16:19
16JYJmnwqeQ = 2 years ago = See a heart surgery being planned with HoloLens 2 - Scott Leaman - NDC Oslo 2020 = 8:38
p8f2iqz2pNQ = 2 years ago = Confessions of a reformed pentester - Nick Murison - NDC Oslo 2020 = 11:39
5JFBRCPhBxM = 2 years ago = Pull Requests: Merge With Your Team - Eirik Isene - NDC Oslo 2020 = 11:15
Owmoge-rTEs = 2 years ago = My experiences using Azure Blueprints for a year - Børge Wiik - NDC Oslo 2020 = 12:21
ncdRDv6sV1A = 2 years ago = Beyond LINQ: Using Expression Trees in .NET - Max Arshinov - NDC Oslo 2020 = 42:35
f18EU9ebO9Q = 2 years ago = Choosing The Best Mobile Framework - Brandon Minnick = 1:00:11
qEV8Oo_Bmws = 2 years ago = Don’t Drop ACID - Transactions in Distributed NoSQL - Matthew Groves - NDC Oslo 2020 = 57:53
qdD0JFo-eZw = 2 years ago = Billions of records: the real success story using Microsoft Power BI Embedded - Irina Dragunova = 56:35
ZcF0-kTHOhE = 2 years ago = Complex systems design in nature - Ian Johnson - NDC Oslo 2020 = 51:04
yUBJh6V5dtI = 2 years ago = Smart home from scratch - Nir Dobovizki - NDC Oslo 2020 = 47:09
JI9b_skMQJ4 = 2 years ago = Event-driven computing with Kubernetes - Jakob Ehn - NDC Oslo 2020 = 59:46
Ki0_0suAN9Q = 2 years ago = The Accidental Security Professional - Elin Tøndel - NDC Oslo 2020 = 10:16
JBSIdlWJcSU = 2 years ago = Capability Mapping - Ian Cooper = 55:19
nxuSMtWGZjc = 2 years ago = Total Rewrite: A Story About F# and Azure Functions in Production - Almir Mesic - NDC Oslo 2020 = 10:59
vVEmElZdjPU = 2 years ago = Serving election results to an entire nation - Hallstein Brøtan - NDC Oslo 2020 = 10:59
I6d6zpgN0Ds = 2 years ago = Improve the illusion of speed - Optimize your web experience to perfection! - Marius Røed - NDC Oslo = 12:34
V2fbVYKby9w = 2 years ago = High Level Advise for your Cloud Security Strategy - Andreas Lohne - NDC Oslo 2020 = 9:12
8J-LBH4QTqE = 2 years ago = Fighting Back Against a Distracted World - Increasing your Focus and Self-motivation - NDC Oslo 2020 = 1:03:42
3U4p8J5zmFM = 2 years ago = Headless CMS and Decoupled CMS in .NET Core - Ruby Jane Cabagnot = 8:47
nw93MScJkqc = 2 years ago = What's it like to attend NDC Sydney Online? = 2:13
dS_o5d6ajT8 = 2 years ago = Making your interns succeed! - Sara Bergman - NDC Oslo 2020 = 10:12
pYjuYqfXtL4 = 2 years ago = This Startup Life: 3 Years Deep - Ben Cull - NDC Oslo 2020 = 58:02
kIDRMhYGkkM = 2 years ago = DIY security and privacy: roll your own VPN in 10 minutes - Jonas Nordstrand - NDC Oslo 2020 = 9:22
Zk3lerO6V8s = 2 years ago = Death of a Craftsman: A software developer identity crisis - Einar Høst - NDC Oslo 2020 = 10:51
idEbonBdF_g = 2 years ago = Considerations for a large-scale low-latency system - Helge Grenager Solheim - NDC Oslo 2020 = 10:12
iUBX4vO8B1k = 2 years ago = When each millisecond counts? - Dmitry Konovalov - NDC Oslo 2020 = 12:17
ajW011aaX4s = 2 years ago = Breaking the build with K6 load tests - Lars Jakobsen - NDC Oslo 2020 = 13:33
eTH4F6XxygE = 2 years ago = How we saved the Black Friday sales for a major jewelry shop - Niklas Bae Pedersen - NDC Oslo 2020 = 6:51
pgMOJdesQvw = 2 years ago = Immutable Infrastructure on Azure - Evgeny Borzenin - NDC Oslo 2020 = 52:31
a2tb3gBzxzo = 2 years ago = Building a Better GitHub Pages Experience Using Azure Services, How Hard Can It be? - Chris Klug = 59:27
rkS-SMA3lUE = 2 years ago = Refactoring the Architect’s role - Yogi Aradhye - NDC Oslo 2020 = 57:47
LdY_HPPpxVo = 2 years ago = “OAuth 2.1” and beyond - Dominick Baier - NDC Oslo 2020 = 57:36
Q3LPj9hMi-U = 2 years ago = Fluxing Up Your .NET Apps - Alex Dunn - NDC Oslo 2020 = 56:04
2kcOdYpT_b4 = 2 years ago = Building a real-time serverless app in Blazor using AWS - Martin Beeby. -NDC Oslo 2020 = 1:01:00
w9T8pSVcX3Q = 2 years ago = Analyzing source code using Roslyn - Erik Schierboom - NDC Oslo 2020 = 1:07:32
rCKPgu4DvcE = 2 years ago = The Power of Composition - Scott Wlaschin - NDC Oslo 2020 = 1:01:36
rdr4RMAAYwA = 2 years ago = Agile is a Dirty Word - James Birnie = 48:41
us4dp7Ksly0 = 2 years ago = Functional data that adapts to change - Don Syme - NDC Oslo 2020 = 45:05
WpfJ86_DYfY = 2 years ago = Kafka as a Platform: the Ecosystem from the Ground Up - Robin Moffatt - NDC Oslo 2020 = 1:00:00
mC5M1AXHko4 = 2 years ago = Learning from Disaster - Ian Hughes = 55:57
0vl-4OhPyQY = 2 years ago = OpenMetrics, OpenTracing, OpenTelemetry - are we there yet? - Alexey Zimarev - NDC Oslo 2020 = 1:02:19
OlfY5GHSrQs = 2 years ago = The Developer's Field Guide to Software Security - Jennifer Janesko - NDC Oslo 2020 = 57:06
LLdU3OnJ83Q = 2 years ago = Embracing Simplicity - Guilherme Ferreira - NDC Oslo 2020 = 49:31
r5nhhaI2__U = 2 years ago = Top 5 Things to do Today to Give Your Users a Better Experience - Billy Hollis - NDC Oslo 2020 = 1:01:03
JcNRXXlLzBM = 2 years ago = Measuring DevSecOps: building metrics to understand effectiveness and success  - Victoria Almazova = 47:48
xHUHlfao3L4 = 2 years ago = Autism in Tech - Dennie Declercq - NDC Oslo 2020 = 58:18
CZz5yfsHFYM = 2 years ago = From Devops to DevSecOps - Bruno Amaro Almeida - NDC Oslo 2020 = 41:59
2XRaW9ATTCI = 2 years ago = DevOps in Real Life, A How-To - Ola Petersson & Jessica Andersson - NDC Oslo 2020 = 53:45
bevn2heQM9Y = 2 years ago = Introduction to GitHub Actions - Edward Thomson - NDC Oslo 2020 = 59:05
y13nT9ihVlA = 2 years ago = The leadership balancing act - achieving success without burning out - Donna Edwards - NDC Oslo 2020 = 55:33
gpT8uieBqX0 = 2 years ago = E2E testing goes Corporate - Björn Weström - NDC Oslo 2020 = 51:10
Vq24Htx3pVE = 2 years ago = Cardboard boss - Elise Garborg Undheim - NDC Oslo 2020 = 7:51
yIDwBaNBinc = 2 years ago = NDC Minnesota - Online - 8-11 September 2020 = 0:30
Tyt8QP6YxtU = 2 years ago = Infrastructure as Software - Paul Stack - NDC Oslo 2020 = 43:49
ptXss2Vp1Ws = 2 years ago = Ring-fence the Chaos: When Technical Teams Meet Organisational Systems - Anthony Dang = 41:59
FD5fX02QCmY = 2 years ago = Feature flags: the toggle, the A/B test and the canary - Santosh Hari - NDC Oslo 2020 = 1:08:38
sOkgaWzMuOA = 2 years ago = The "Guilded" Age: How a UX Guild can transform design at your company - Ash Banaszek = 50:55
T5DsrO7xv8E = 2 years ago = Let’s stop blaming our users for getting hacked when it is our problem to solve - Scott Brady = 46:47
c0kDytN8LC0 = 2 years ago = Quantum Computing Deep Dive - Johnny Hooyberghs - NDC Oslo 2020 = 1:02:20
XAPP-hM4ZPQ = 2 years ago = Reducing Third-Party Security Risk in .NET Core Applications - Niels Tanis - NDC Oslo 2020 = 58:37
1bH-5ijV9Fs = 2 years ago = From WCF to gRPC - Mark Rendle - NDC Oslo 2020 = 1:01:16
-LmYN7CKCbY = 2 years ago = Real rebels pay their taxes - Nils Norman Haukås - NDC Oslo 2020 = 47:48
PgwEXcTvyhg = 2 years ago = Build a DevOps Culture: Microsoft's Journey to adopt an Agile Mindset and DevOps culture - Gousset = 1:02:17
F4ZYmRFVHZI = 2 years ago = The Art & Joy of Testing in Production - Geert van der Cruijsen - NDC Oslo 2020 = 1:01:38
WY0Eo2vsOJg = 2 years ago = Building an open source government application platform in the cloud - Buadu, Larsen & Kylstad = 1:00:15
qyi1RbC3qrg = 2 years ago = Megahertz, Gigahertz, Registers and Instructions: How does a CPU actually work? - Kendall Miller = 1:01:56
A77qv1hz_50 = 2 years ago = What is a software security initiative and do I need one? - Nick Murison - NDC Oslo 2020 = 52:49
_QnbV6CAWXc = 2 years ago = F# as a Better Python - Phillip Carter - NDC Oslo 2020 = 1:00:30
kLhoRyLxwAE = 2 years ago = Modern Web UI with Blazor WebAssembly - Steve Sanderson - NDC Oslo 2020 = 56:19
VGl2w4KNVAQ = 2 years ago = Does Your Codebase Spark Joy? - Jenna Pederson - NDC Oslo 2020 = 1:01:04
Rm3IOOZSPEw = 2 years ago = Do Developers Dream of Stateless Apps? - Łukasz Gebel - NDC Oslo 2020 = 45:01
n52GkwxSJdY = 2 years ago = Domain Driven UI - Roman Sachse - NDC Oslo 2020 = 56:18
LfrELxJuoyA = 2 years ago = Chinafy your apps + Lessons you can steal from China - Adam Cogan - NDC Oslo 2020 = 1:01:12
ipeWGx3oj4A = 2 years ago = Where's my Stuff? Exploring data storage options in Azure - Mike Benkovich - NDC Oslo 2020 = 54:08
tqwcz-Yt9gQ = 2 years ago = Building confidence in concurrent code with a model checker - Scott Wlaschin - NDC Oslo 2020 = 1:04:08
yXKkBgXJANM = 2 years ago = A Tale Of Four Startups - Liam Westley - NDC Oslo 2020 = 1:05:21
8wYWTTfKjUU = 2 years ago = Welcome to the (state) machine - Mauro Servienti - NDC Oslo = 57:49
TZG3OGlrzIQ = 2 years ago = OpenID Connect & OAuth 2.0 – Security Best Practices - Dominick Baier - NDC Oslo 2020 = 1:02:14
qSVgshwVP_s = 2 years ago = Safety-critical systems from the inside - Maciej Gajdzica - NDC Oslo 2020 = 58:20
eDbsOxGjqSc = 2 years ago = Make it Boring - Jeremy Wagner - NDC Oslo 2020 = 39:58
Rrl_QxPX248 = 2 years ago = Type-setting in CSS: Using typography to enhance your design - Martine Dowden - NDC Oslo 2020 = 50:24
w-tgwwAR8_Y = 2 years ago = Authoring ARM templates the easy way with FARMer - Isaac Abraham = 57:26
T6NRcX1vnz8 = 2 years ago = Clean Testing - Clean Architecture with .NET Core - Jason Taylor - NDC Oslo 2020 = 1:03:40
yr_VFiv1Gmo = 2 years ago = How Sigmund Freud would perform a code review? - Piotr Czajka - NDC Oslo 2020 = 1:02:32
_dQRAsVhCqA = 2 years ago = Domain-Driven Refactoring - Jimmy Bogard - NDC Oslo 2020 = 1:02:24
0UZf_7c_EeE = 2 years ago = Anatomy of ASP.NET Core Requests - Steve Gordon - NDC Oslo 2020 = 57:36
cDpkzfiLY0M = 2 years ago = Kiss My Sass - Martine Dowden - NDC Oslo 2020 = 51:12
XgPRWcX4sYU = 2 years ago = Reinforcement Learning: Pac-Man - Malte Loller-Andersen & Manu Gopinathan - NDC Oslo 2020 = 1:01:10
WlsetrZgSMQ = 2 years ago = GraphQL, gRPC or REST? Resolving the API Developer's Dilemma - Rob Crowley - NDC Oslo 2020 = 59:09
glPrWPr-IPc = 2 years ago = Designing and rewriting asynchronous tasks from scratch - Kevin Gosse - NDC Oslo 2020 = 59:30
arftH99r_Xk = 2 years ago = Why you should consider Web Assembly in your next frontend project - Håkan Silfvernagel = 36:08
HhpfkdP913k = 2 years ago = The 5 Pillars of Collaborative Product Ownership - John Le Drew - NDC Oslo 2020 = 58:36
TKyzGoR0WQE = 2 years ago = Strangling Hydra one head at the time - Markus Fanebust Dregi - NDC Oslo 2020 = 39:17
mKdXhjUopCA = 2 years ago = A Brief History of Computer Music - Anders Norås - NDC Oslo 2020 = 48:11
VKQAS3PNEVw = 2 years ago = Compassionate Components - Kristofer Selbekk - NDC Oslo 2020 = 39:54
I4T7kTRqeMw = 2 years ago = Going fast and cheap with Bots, Sanity and Kubernetes - Olav Nybø - NDC Oslo 2020 = 48:46
6FBmeTGN5Pk = 2 years ago = TDD and the Terminator - An introduction to Test Driven Development - Layla Porter - NDC Oslo 2020 = 54:34
MtyOlYzT62M = 2 years ago = Future-Proof Mobile Cross-Platform Apps with Flutter - Christian Wenz - NDC Oslo 2020 = 1:00:10
KEji1OmpJYA = 2 years ago = Continuous Delivery with Azure Web Apps - Vidar Kongsli - NDC Oslo 2020 = 53:03
yP7DAdZAdTw = 2 years ago = How Effective Teams Use Git - Enrico Campidoglio - NDC Oslo 2020 = 1:07:49
CX8UfflxVMI = 2 years ago = Who's your user? OpenID from the ground-up - Johannes Brodwall - NDC Oslo 2020 = 46:41
5kOzZz2vj2o = 2 years ago = Vertical Slice Architecture - Jimmy Bogard = 1:02:50
1Hz4Pnph0N8 = 2 years ago = Continuous Delivery For Machine Learning: Patterns And Pains - Emily Gorcenski = 44:06
vNhnR50zLzk = 2 years ago = Continuous Intelligence: Keeping your AI Application in Production - Emily Gorcenski & Arif Wider = 57:39
6czpapfDu-c = 2 years ago = ASP.NET Core Beyond the Basics - Chris Klug = 1:00:24
Pw-RQ34tWa8 = 2 years ago = Build Your Cloud Infrastructure as Code With .Net Core - Hossam Barakat = 48:06
t6OQADJCRSk = 3 years ago = Event-driven computing with Kubernetes - Jakob Ehn = 56:58
1rb0wHB_jBY = 3 years ago = .NET Core Data Security : Hope is not a Strategy - Stephen Haunts = 1:00:35
I9mJ-ra3ACY = 3 years ago = Three years of lessons from running potentially malicious code inside containers - Ben Hall = 1:02:10
s2N4ciMqS-E = 3 years ago = Let's fly a drone with AI, and a bit of JavaScript - Yaser Adel Mehraban = 40:55
Ur15yeiDXYI = 3 years ago = Consuming Microservices - Ian Cooper = 1:01:46
uJvwMWojePU = 3 years ago = Keynote - Developing on Windows (and Linux) (and Remotely) in 2020 - Scott Hanselman = 58:34
KuaDheLcLdo = 3 years ago = How to Build an Inaccessible App - Amy Kapernick = 1:02:28
_S9nRV0xU1I = 3 years ago = NDC Melbourne Online - 27-30 July 2020 = 0:30
n-N67Q0O52U = 3 years ago = JavaScript: Past, Present and Future - David Neal = 47:27
IYzDFHx6QPY = 3 years ago = The lazy programmer's guide to writing thousands of tests - Scott Wlaschin = 52:51
w2zelM--qHw = 3 years ago = Implementing OpenID Connect and OAuth 2.0 – Tips from the Trenches - Dominick Baier = 1:01:55
-lsTl2_Z-tY = 3 years ago = Measuring DevSecOps: building metrics to understand effectiveness and success. - Victoria Almazova = 52:50
Bwqsqvw46k4 = 3 years ago = What You Need to Know About Open Source—Trust Me, I'm a Lawyer - Jeffrey Strauss = 57:44
AsT4bCM4tJc = 3 years ago = The Mentor Playbook - Gabriela Dombrowski = 43:03
VvYzfmTWCS8 = 3 years ago = Real World Guide to Web API authentication on Azure - Heather Downing = 43:27
cX306jgUlQk = 3 years ago = AI in the battle against fakes. - Henk Boelman = 1:00:14
MKqoCjxkuJk = 3 years ago = Hot Chocolate: An introduction to GraphQL on ASP.Net Core - Michael Staib = 55:04
djCFYbmmfeM = 3 years ago = Forget about HTTP - Irina Scurtu = 1:00:51
1bGFawyKlIw = 3 years ago = NDC OSLO 2020 -  Online event = 0:30
jw8yK5JV0xw = 3 years ago = How Effective Teams Use Git - Enrico Campidoglio = 1:04:19
-6AGB3pEMzs = 3 years ago = From the OWASP Top Ten(s) to the OWASP ASVS - Jim Manico = 20:52
yrAUxjbdJmQ = 3 years ago = TypeScript for F# zealots - Tomas Petricek = 1:02:51
pHAlDVL1Yrs = 3 years ago = How to migrate an existing application to serverless - Marcia Villalba = 55:01
Q1BW9RDYFgQ = 3 years ago = Breaking black-box AI - Evelina Gabasova = 59:58
WBos6gH-Opk = 3 years ago = C# into the Future - Mads Torgersen = 1:00:36
WuPC5w9EgVw = 3 years ago = Deep Dive on Server-Side Blazor .NET - Carl Franklin = 1:00:33
sAAo6JeklDw = 3 years ago = The Abridged History of Application Security - Jim Manico = 27:47
RvMRZknzRm8 = 3 years ago = NDC Oslo Online - 8-12 June 2020 = 0:16
pkxyiF32fHE = 3 years ago = What you always wanted to know about Deep Learning, but were afraid to ask - Wei Meng Lee = 58:25
9bNuC5K7qEU = 3 years ago = Confusion In The Land Of The Serverless - Sam Newman = 1:00:28
HiDqrqa34Ls = 3 years ago = Cultivating Production Excellence - Liz Fong-Jones = 47:06
MS1GXQfUZlA = 3 years ago = Measuring DevSecOps: building metrics to understand effectiveness and success - Victoria Almazova = 50:40
hJ35xBi4KJc = 3 years ago = Top Secret Cloud Native Security Lessons - Ben Hall = 58:02
yXixyZ5ch3c = 3 years ago = How Effective Teams Use Git - Enrico Campidoglio = 1:08:22
Z1gWfvPXDQo = 3 years ago = Octopus Runbooks, putting the Ops in DevOps - Derek Campbell = 51:03
mukFFVM-jgg = 3 years ago = Infrastructure as code - is it really? - Shahid Iqbal = 52:54
CKLIL3Kbf60 = 3 years ago = Microservices and Serverless - Sam Newman = 1:00:05
VXKTrx7qcVM = 3 years ago = Database Deployment Cowboys to Continuous Delivery Heroes - Adam Close = 48:22
kIF2sj2IPV8 = 3 years ago = It's A Trap! - Sam Newman = 59:02
g_7pYAfx0kQ = 3 years ago = Using Immutable Data Structures in C# and .NET - Spencer Schneidenbach = 47:27
jA72XrgB_gw = 3 years ago = Reducing Third-Party Security Risk in .NET Core Applications - Niels Tanis = 57:34
C0wN5rxKt6E = 3 years ago = Introducing the benefits of the testing diamond - Moreton Brockley = 42:26
WdMQilEWet4 = 3 years ago = Fighting Back Against a Distracted World - Increasing your Focus and Self-motivation -Stephen Haunts = 1:00:28
qgTmut8Y9Lo = 3 years ago = The Rise of Klintwalker – Mastering Your Inner Developer Part 2 - Lars Klint = 58:14
Q_DAn3EvYvY = 3 years ago = Modernizing Large Frontends with Web Components - Sam Julien = 56:14
l_P6m3JTyp0 = 3 years ago = GraphQL, gRPC or REST? Resolving the API Developer's Dilemma - Rob Crowley = 59:26
pxDczZYe6F8 = 3 years ago = Lowering in C#: What's really going on in your code? - David Wengier = 44:39
mjB2j7Anirw = 3 years ago = Who’s not in the room? Build better products by engaging hard to reach users - Ariba Jahan = 34:32
ERhZjJbqUbo = 3 years ago = Big Data Analytics in Near-Real-Time with Apache Kafka Streams - Allen Underwood = 1:01:53
zySHbwl5IeU = 3 years ago = Getting the best out of Entity Framework Core - Jon P Smith = 1:00:12
cRPUHxmGcjo = 3 years ago = The Perimeter Has Been Shattered: Attacking and Defending Mobility and IoT on the Enterprise Network = 53:48
6avJHaC3C2U = 3 years ago = The Art of Code - Dylan Beattie = 1:00:49
gJV30GTQE7I = 3 years ago = Combatting illegal fishing with Machine Learning and Azure - Carmel Eve & Jess Panni = 46:09
yTtZQVSnz2M = 3 years ago = A tale of two sides of 2FA - Christine Seeman = 49:49
2tFj0xR9Pf0 = 3 years ago = Drinking a river of IoT data with Akka.NET - Hannes Lowette = 58:41
dDZNDVO5EFQ = 3 years ago = Common API Security Pitfalls - Philippe De Ryck = 49:32
AGB3Ml_mIWc = 3 years ago = ML and the IoT: Living on the Edge - Brandon Satrom = 1:01:14
Y7StjYhXvpE = 3 years ago = Lambda? You Keep Using that Letter - Kevlin Henney = 1:00:53
2b7S0bDO0jw = 3 years ago = How to Build a Magical Living Room - Saron Yitbarek = 34:53
HdXDSjWe2Q8 = 3 years ago = Continuous Integration and Delivery for Databases - Jimmy Bogard = 59:42
KPmX2nAPSOo = 3 years ago = How To Secure Your MicroServices - Andy Davies = 37:59
0o8wIMnqH64 = 3 years ago = Test Driven Compliance - Mike Long = 10:06
uwJI-_08mCs = 3 years ago = Five Ways to Break a Git Repository - Edward Thomson = 14:15
if5YLYRIcc8 = 3 years ago = How to train your impostor - Carolina Gilabert = 8:12
80H-9caP7UM = 3 years ago = UX Design Fundamentals: What do your users really see - Billy Hollis = 1:05:18
JrA1cv5jvFA = 3 years ago = Deep Dive on Server-Side Blazor - Carl Franklin = 1:00:10
SNfXz-NOZ5s = 3 years ago = Crash, bang, wallop: miscellaneous lessons from exploring a drum kit - Jon Skeet = 1:02:47
NGysckR7idA = 3 years ago = The Reduced NDC Company - Mark Rendle = 1:08:15
XnpFEegjVI4 = 3 years ago = Fly the Enterprise: Applying Aviation Lessons to DevOps Teams - Kendall Miller = 1:01:05
USSkidmaS6w = 3 years ago = Reinventing the Transaction Script - Scott Wlaschin = 1:01:04
CQMVOCTBYRA = 3 years ago = Breaking black-box AI - Evelina Gabasova = 51:39
Z3G5SJQVMno = 3 years ago = Navigating microservices with .NET Core - Ryan Nowak = 1:03:37
3Wx1AsYV6YE = 3 years ago = Building Trust in Teams - Richard Campbell = 55:50
DH2yUVQDB0I = 3 years ago = Single Page Architectures with VueJS and ASP.NET Core - Kevin Griffin = 1:01:00
UXeFR5RQnjs = 3 years ago = Go Pro on .NET with F# - Isaac Abraham = 1:05:47
PLFLTMHB5Do = 3 years ago = Serverless containers with Knative and Cloud Run - Mete Atamel = 1:01:07
ZWxuEySnc60 = 3 years ago = How does designing your culture help your code? - Vimla Appadoo = 45:30
JHhtGfjFWyM = 3 years ago = How to hire great engineers - Norman Noble = 1:01:47
W3I8VOCgvys = 3 years ago = Building a real-time serverless app in Blazor using AWS - Martin Beeby = 57:01
WHL2v4mXbRE = 3 years ago = 3D printed Bionic Hand a little IOT and a Xamarin Mobile App - Clifford Agius = 59:26
UmNxlSrn8Mc = 3 years ago = Alexa, ask Cortana to tell Google to... - Alex Dunn = 53:57
zLB2_h-3ZS4 = 3 years ago = Challenges of Managing CoreFX repo - Karel Zikmund = 1:07:51
pjA_W6PUbOk = 3 years ago = Sprinkle some sparkle on it: Teaching Xamarin with Selfies - Luce Carter & Layla Porter = 58:00
WGMIcXMeYqA = 3 years ago = Ordering the chaos - cleaning logs and ordering events in microservices - Adam Furmanek = 55:38
pcsBqt4Qjbc = 3 years ago = Real World Guide to Web API authentication on Azure - Heather Downing = 41:07
OlvVS0Xl6EA = 3 years ago = Angular and The Case for RxJS - Sandi Barr = 58:29
dQi66iTLxsc = 3 years ago = How Does Data Science Revolutionize the World of Machines? - Victoriya Kalmanovich = 28:42
hqWIdaAjdmI = 3 years ago = How to code music? - Laura Silvanavičiūtė = 39:12
aHsVsbo_VOE = 3 years ago = Effective Microservice Communication and Conversation Patterns - Jimmy Bogard = 58:57
kCB2WezkFwI = 3 years ago = Svelte, cybernetically enhanced web apps - Devlin Duldulao = 40:29
WqibJHxQ5wU = 3 years ago = Solving Tricky Coordination Problems in Stateless .NET Services - Loris Cro = 55:43
-__TNwVR110 = 3 years ago = Wait, I have to test the front end too? - Amy Kapernick = 48:41
jtzwGXw-FkU = 3 years ago = Introduction to GitHub Actions - Edward Thomson = 59:42
eiUgVa2Td_k = 3 years ago = The State of Vue.js in 2020 - Why You Should Make The Leap - Gwendolyn Faraday = 49:26
RZT3md8Eo4Q = 3 years ago = Shrink The Web: How To Get Happier By Removing Crap - Lemon = 52:49
CwISe8blq38 = 3 years ago = Turbocharged: Writing High-Performance C# and .NET Code - Steve Gordon = 1:01:12
Do0RfWqXtvw = 3 years ago = 25 Years of SSL - Secure(ish) Sockets Layer - Scott Helme = 1:00:14
JYutd5p0XYk = 3 years ago = Best practices for securing CI/CD pipeline - Victoria Almazova = 49:40
gf5THQN9nQk = 3 years ago = Turning a side project into a business 10 lessons in 10 minutes - David James = 12:54
PumU-0nYA7w = 3 years ago = The monster under the bed - working with legacy code - Ioana Bota = 10:40
6hcpohbbM44 = 3 years ago = OWASP ZAP HUD WTF? - Robin Minto = 11:32
bUMmj85UiXM = 3 years ago = Keep it Clean: Why Bad Data Ruins Projects and How to Fix it - Philip Winder = 49:20
QnBYmTpugz0 = 3 years ago = Blazor in more depth - Ryan Nowak & Steve Sanderson = 1:02:12
CCIO3GOaFe0 = 3 years ago = From the OWASP Top Ten(s) to the OWASP ASVS - Jim Manico = 1:01:47
aUbXGs7YTGo = 3 years ago = Change your habits: Modern techniques for modern C# - Bill Wagner = 55:46
5Iy0hHLHrCg = 3 years ago = DDD Really Matters! - Jimmy Nilsson = 1:02:04
CtFYlZE6ItQ = 3 years ago = Why Kubernetes is Not Enough - Gaurav Gupta = 45:40
0Aqy8h0W3RQ = 3 years ago = Beyond REST with GraphQL in .Net core - Irina Scurtu = 58:18
TxooPnte1NI = 3 years ago = Machine Learning for .NET developers - Olia Gavrysh = 45:01
FRsRoaubPiY = 3 years ago = The Internet of Pwned Things - Troy Hunt = 59:16
d7YCNbXurp0 = 3 years ago = Can TypeScript really make infrastructure management easy? - Paul Stack = 1:01:00
TQoABqkPkAE = 3 years ago = Micro Frontends – a strive for fully verticalized systems - David Leitner = 57:00
Z46l08O3DKo = 3 years ago = Frontend in F#? Hold my beer! - Vagif Abilov = 50:26
3QHVPjMbGVQ = 3 years ago = An introduction to Machine Learning using LEGO - Jeppe Tornfeldt Sørensen = 57:44
3UH9oEBc7XE = 3 years ago = Delightful Durable Function Patterns - Adrienne Tacke = 47:49
pG75qjEBkC4 = 3 years ago = Empowering Soft Skills with Team Dynamics/Communication Skills - Crux Conception = 58:47
AL07H9Vjwtw = 3 years ago = A Developer's Introduction to Electronics - Guy Royse = 53:56
fWtu-DyncWQ = 3 years ago = Frictionless Frontends for Backend Developers - Mandy Michael = 50:39
PwQSmbzBsvE = 3 years ago = Modernizing the enterprise desktop application - Oren Novotny = 1:01:28
VNcMJlFRZaA = 3 years ago = Shor's Algorithm is Scary NOW - James Birnie = 56:33
0S7EI_szVY4 = 3 years ago = Serverless: Five Key Things you need to Know - Gojko Adzic = 58:14
zyUwR2PL7xI = 3 years ago = There’s an Imposter in this room! - Angharad Edwards = 56:23
76X9oo-LlUY = 3 years ago = From WCF to gRPC - Mark Rendle = 1:04:33
lAyL9HKx8cQ = 3 years ago = A Developer’s Introduction to Kubernetes - Chris Klug = 1:00:08
6FfKjAXFNzk = 3 years ago = Cynicism Doesn’t Build Products - Gwen Diagram = 40:56
LLkf8lBLT7E = 3 years ago = Controlling Wildfires While Only Getting Singed. - Jessica White = 40:15
6pjAjHm7l7s = 3 years ago = Capability Mapping - Ian Cooper = 1:01:11
PIj0TaH6MH4 = 3 years ago = How to Steal an Election - Gary Short = 1:02:35
zyTDEa-ReVg = 3 years ago = What you always wanted to know about Deep Learning, but were afraid to ask - Wei-Meng Lee = 1:03:31
m3m9aKFjLEc = 3 years ago = There are no snow days when you work remote. - Jennifer Wadella = 55:13
_b60NQNdg7A = 3 years ago = EVE Online: Defending our players from hackers and the evolution of account security = 50:30
AUgZffkurK0 = 3 years ago = OpenID Connect & OAuth 2.0 – Security Best Practices - Dominick Baier = 52:58
fnkTw8Vmmig = 3 years ago = Lean, not mean. Building sustainable software with Lean software practices - David James = 10:22
sLR_12ID1e0 = 3 years ago = Using cats to purfect your software architecture - Andy Clarke = 13:49
1OUdJipI7-0 = 3 years ago = Debugging - A dive into Breakpoints - Philip Sutton = 4:34
ke1sel87Rsg = 3 years ago = Securing Serverless Applications in Azure - Sjoukje Zaal = 59:41
Khn7sDUSEJM = 3 years ago = Blazor, a new framework for browser-based .NET apps - Steve Sanderson = 1:01:13
0Y-Pjr0abWQ = 3 years ago = Rip It Up And Start Again? - Sam Newman = 1:01:12
VmkEUpY6HeY = 3 years ago = : The OWASP Top Ten Proactive Controls 2018 - Jim Manico = 58:00
p6CjlnwPhHQ = 3 years ago = Application Diagnostics in .NET Core 3.1 - Damian Edwards & David Fowler = 1:00:45
zVbTmgbiZsA = 3 years ago = Make your custom .NET GC - "whys" and "hows" - Konrad Kokosa = 49:15
iL9nLAjCPtM = 3 years ago = SignalR Deep Dive: Building Servers - David Fowler & Damian Edwards = 59:01
2YjrmgFJ_S8 = 3 years ago = We are the Guardians of our Future - Tess Ferrandez-Norlander = 50:55
OKRytoQAw-4 = 3 years ago = The Cyberattack on Visma in 2018, experience sharing and views from the blue team - Espen Johansen = 44:33
mY4ifhgpbf8 = 3 years ago = .NET Core Data Security : Hope is not a Strategy - Stephen Haunts = 52:12
QpkVnB-N20c = 3 years ago = Implementing OpenID Connect and OAuth 2.0 – Tips from the Trenches - Dominick Baier = 1:00:24
yqqhrrZK62Q = 3 years ago = Designing a Secure Software Development Lifecycle with DevOps - Mike Long = 48:07
vbQFmDQxnCY = 3 years ago = Modern Web Vulnerabilities 2020 - Erlend Oftedal = 56:14
hlEzlS6WN4k = 3 years ago = Common API Security Pitfalls - Philippe De Ryck = 53:13
i-Nzx_FSlug = 3 years ago = The Future of AppSec is Cloud-Native - Jimmy Mesta = 55:56
jeRALmfyoqg = 3 years ago = OpenID Connect & OAuth 2.0 – Security Best Practices - Dominick Baier = 59:28
7SynByU5S4E = 3 years ago = The Internet of Pwned Things - Troy Hunt = 1:01:27
u0qYcMYoERU = 3 years ago = Why Don't Users Do What They are Supposed to Do? A look at users and security - Silje Lærk = 1:02:40
zb2f2FUiAUs = 3 years ago = 25 Years of SSL - Secure(ish) Sockets Layer - Scott Helme = 52:49
6PGvWSH5i7Y = 3 years ago = Measuring DevSecOps: building metrics to understand effectiveness and success - Victoria Almazova = 45:43
V0rb4SbvuJs = 3 years ago = A reasonable guide to security practices - Niall Merrigan = 1:01:56
8qr_jCKGL_E = 3 years ago = Introduction to Election Security - Patricia Aas = 1:02:22
Nj_MKm_0V0M = 3 years ago = Keynote: Post Quantum Future - Jaya Baloo = 40:50
vN9OP7iwTSQ = 3 years ago = NDC Melbourne 2020 = 0:33
tqtOo73fyOE = 3 years ago = NDC Sydney 2020 = 1:14
dCgqTDki-VM = 3 years ago = Blazor in more depth - Steve Sanderson & Ryan Nowak = 1:03:04
FW9ngRnBXss = 3 years ago = Beyond infrastructure as code DSLs - Jake Ginnivan = 1:02:17
5OtUm1BLmG0 = 3 years ago = Clean Architecture with ASP.NET Core 3.0  - Jason Taylor - NDC Sydney 2019 = 1:02:30
31ZllVe-rXs = 3 years ago = Unity for the enterprise developer - Matt Ellis = 55:55
3_zCtScT05Y = 3 years ago = NDC Sydney 2019 Lightning Talks - Has AlTaiar, Michael John Pena, Negar Ghanbari & Vatsalya Goel = 40:34
HpwK-K-BumY = 3 years ago = Access All Areas: Making Accessibility More Accessible - André Lemos = 39:58
JpM95-Wplzo = 3 years ago = gRPC for ASP.NET Core, a new framework for high performance APIs - James Newton-King = 1:01:10
LUIluMm01xw = 3 years ago = Busting the Func'ing Jargon - Daniel Chambers = 1:04:53
ciuNxlMm358 = 3 years ago = Tackling Dreaded .Net Cold Starts When Going Serverless - Sarjeel Yusuf = 56:51
-pItpHq7X1w = 3 years ago = Modern day C# development in Visual Studio 2019 - Kevin Pilch = 1:01:17
1R4itvhkTI0 = 3 years ago = Introduction to Angular 8 - Alain Chautard = 59:39
1sPpal7nO98 = 3 years ago = C# 8 and Beyond - Filip Ekberg = 55:36
320aB4fgJRs = 3 years ago = Being cheap with the cloud - Aaron Powell = 58:43
3Gonh1afx2g = 3 years ago = Apache Kafka Event streaming platform for .NET developers - Viktor Gamov = 1:02:47
4g0yaATi31w = 3 years ago = EVE Online: Defending our players from hackers - Stefán Jökull Sigurðarson = 42:55
61ArSpwDRFE = 3 years ago = A brief history of Cloud - Alex Mackey = 59:56
6BT2AF9PO5g = 3 years ago = Blazor, a new framework for browser-based .NET apps - Steve Sanderson = 1:01:28
6PZ0HjZJssY = 3 years ago = Full Stack Accessibility, and the Business Case for being Inclusive - Larene Le Gassick = 1:00:37
7dJBmV_psW0 = 3 years ago = The next 5 years of ASP.NET Core - Ryan Nowak = 1:01:20
A1spVklTgw4 = 3 years ago = Monitoring a Global Multitenant Service - Magnus Mårtensson = 1:00:05
AIGps2KU-DQ = 3 years ago = Hack to the Future - Troy Hunt = 1:00:15
AOKYhTMrWr4 = 3 years ago = Bank Grade Security - Kieran Jacobsen = 48:00
EpYYe6aQjJM = 3 years ago = Static Sites, Dynamic microservices, & Azure: How we built Microsoft Docs and Learn - Dan Fernandez = 1:02:56
F-E7VLtRdeE = 3 years ago = The Moon: Gateway to the Solar System - Richard Campbell = 56:02
8anlm2UE7_A = 3 years ago = Service degraded: Tackling burnout in the IT industry - Sonia Cuff = 54:04
JOGIRx3HSTY = 3 years ago = Cloud Governance: Winning the battle between speed and control - Sonia Cuff = 55:11
KGzs3EVS43k = 3 years ago = Getting Started with Cosmos DB + EF Core - Thiago Passos = 1:01:29
Kq0NZ9NdpDs = 3 years ago = So, you want to be a CTO? - Mahesh Krishnan = 1:02:23
LIaekiT6Ehs = 3 years ago = GraphQL, gRPC or REST? Resolving the API Developer's Dilemma - Rob Crowley = 50:53
LrNuz4Tp8U4 = 3 years ago = Going 0 to 100 with Kubernetes - Scott Holden = 1:04:09
Mic9bhZWTas = 3 years ago = Modern JavaScript For Web Dinosaurs - Ryan Preece = 54:20
NUz212O79tE = 3 years ago = Internals of Exceptions - Adam Furmanek = 1:01:26
NtuFfWVJF_w = 3 years ago = Chinafy your apps + Lessons you can steal from China - Adam Cogan = 1:03:37
RFGsqwZYj04 = 3 years ago = Dungeons, Dragons and Functions - Mathias Brandewinder = 59:14
SdXj-2IHhiA = 3 years ago = Real-time Face Recognition With Microsoft Cognitive Services - Jernej Kavka (JK) = 45:00
TYca-xEOX6Q = 3 years ago = Building a Realtime "Backend in a Box" with PostgreSQL and Vue - Rob Conery = 51:18
TgUYcZV-foM = 3 years ago = Async demystified - Karel Zikmund = 47:03
UGPHxyncmYY = 3 years ago = Empower Your Microservices with Istio Service Mesh - Hossam Barakat = 55:19
V_m1i1MkG4Q = 3 years ago = Dissecting Kubernetes (K8s) - An Intro to Main Components - Joshua Sheppard = 44:04
X3fAEiUVw0U = 3 years ago = Reverse Engineering a Classic Video Game - Tim Comport = 59:19
Xs1-OU5cmsw = 3 years ago = DataDevOps for the Modern Data Warehouse on Microsoft Azure - Lace Lofranco = 56:21
Xv28Nv6UqzM = 3 years ago = Serverless and App Service Security on Azure - Pratik Khasnabis & Mahesh Krishnan = 1:03:22
Y1WF2ZB_8Pg = 3 years ago = AI in the battle against fakes - Henk Boelman = 58:32
YrkW3-Px5co = 3 years ago = DDD really matters! - Jimmy Nilsson = 58:06
ZsXr-MprASE = 3 years ago = DevOps for the Commodore 64: so what's your excuse? - Todd Whitehead = 56:44
a0etWuHwN4w = 3 years ago = Opening Doors with JSON Web Tokens - Ben Dechrai = 45:32
aLoEIpidgrI = 3 years ago = Pragmatic DevOps - How and Why - Damian Brady = 1:00:44
ds7wVL4Zb0s = 3 years ago = Kubernetes – going beyond the basics - Shahid Iqbal = 1:00:32
ekNSwDS1ya4 = 3 years ago = Keeping your builds green using Docker - Jakob Ehn = 57:40
enSdwvf6yLM = 3 years ago = Deep Learning with CNTK and F# - Mathias Brandewinder = 54:34
gSqxp2cjSYQ = 3 years ago = I Don’t Need No Stinkin’ Framework - Mastering Shadow DOM - Martine Dowden = 41:42
girnjrfRlNk = 3 years ago = How to put a Penguin in a Cloud: Linux on Azure - Brendan Richards = 1:06:15
h77ERvW5mHI = 3 years ago = API team characteristics and best practices - Nahid Farrokhi = 54:24
jqEvu3IvxlA = 3 years ago = Handling Angular Forms Without Losing Your Sanity - Jennifer Wadella = 48:01
kqdsC_Oj9Gk = 3 years ago = TypeScript - Beyond the Basics - Eric Potter = 50:49
l8jQrPl1JyY = 3 years ago = A Tale Of Four Startups - Liam Westley = 56:43
lCWG2S0FYVI = 3 years ago = Modern day C# development in Visual Studio 2019 - Kevin Pilch = 1:01:17
ncHfFgwDytA = 3 years ago = Using Flutter to develop cloud enabled mobile applications - Pooja Bhaumik & Nick Randolph = 1:06:48
nprLjvbx5P0 = 3 years ago = Commuting like a developer - Anton Ball = 52:08
pKs4OJozxfk = 3 years ago = Innovation and Trends in Cloud Computing - Julio Faerman = 59:22
pyScf-IbMuA = 3 years ago = How to do in-app chaos testing - Wesley Cabus = 57:49
s3cq4sQldcM = 3 years ago = Thousands of concurrent connections with Azure SignalR Service - Nelly Sattari & Stafford Williams = 46:37
sQCRvdBZHKA = 3 years ago = Building Trust in Teams - Richard Campbell = 1:04:14
thkqb9cMBzc = 3 years ago = Containers/Docker - what, why and how - Shahid Iqbal = 1:01:03
ytmD8v7KG3o = 3 years ago = Iterative metrics, dashboards and monitors - Carmel Hinks = 43:45
tzcOeKzM2q0 = 3 years ago = Continuous Intelligence: Keeping your AI Application in Production - Arif Wider = 58:43
ujcp2LiPds8 = 3 years ago = Microservices for building an IDE – The innards of JetBrains Rider - Maarten Balliauw = 51:30
vQXlhPBvjtw = 3 years ago = Quantum Computing Concepts - John Azariah = 59:14
wR9zxqB_r-0 = 3 years ago = Understanding Git — Behind the Command Line - Enrico Campidoglio = 54:41
wz_iNyyQRwM = 3 years ago = Cognitive biases in software development - Ian Hughes = 1:02:12
yhmiWhB9Qns = 3 years ago = Back to Basics: Efficient Async and Await - Filip Ekberg = 57:35
zxSlKiWOOzw = 3 years ago = Azure SpendOps – The Art of Effectively Managing Azure Costs - William Liebenberg = 35:07
ErrWPojWFp4 = 3 years ago = Building Great Teams - Donna Edwards = 59:33
xniolu3w5Ro = 3 years ago = What's going on with Project Fugu? - Phil Nash = 48:47
1AZA1zoP-II = 3 years ago = F# Code I Love - Don Syme = 56:59
kiMPQ9fRIlA = 3 years ago = Renault car infotainment system with TomTom LIVE Services - Peter Bindels = 42:49
VoLHTmJ1Aas = 3 years ago = Freestanding C++ - Past, Present, and Future - Ben Saks = 1:00:56
M-5_M8qZXaE = 3 years ago = Testing The Tests: Mutation Testing for C++ - Seph De Busser = 44:26
4Ap5DNBRIHQ = 3 years ago = The Evolution of Accelerated 2D and 3D Graphics in Qt - Laszlo Agocs = 59:47
ZEAX8CqLQfE = 3 years ago = Uncertain Models - Learning from the past and optimizing for the future - Markus Fanebust Dregi = 40:22
ZJJTIZ8XQvw = 3 years ago = The Dawn of a New Error - Phil Nash = 59:46
6e_dZddKXhQ = 3 years ago = The Anatomy of an Exploit - Patricia Aas = 56:49
soeFwz0cOqU = 3 years ago = Just enough Assembly for Compiler Explorer - Anders Schau Knatten = 59:49
VJ6ZvDRYzNE = 3 years ago = C++ Insights: See your source code with the eyes of a compiler - Andreas Fertig = 58:24
gu7ma2omxS8 = 3 years ago = Reverse engineering a legacy software in a complex system: A systems engineering approach = 29:24
QBllNNnqpHk = 3 years ago = Scaling Qt from Desktop to Servers and Micro-controllers - Volker Hilsheimer = 49:16
Cbln5S0E8Kk = 3 years ago = The ultimate guide to software updates on embedded Linux devices - Mirza Krak = 47:58
mn1ZnO3MtVk = 3 years ago = Embracing Modern CMake - Stephen Kelly = 1:03:00
IepYRiQ7Flw = 3 years ago = Make your tests tell the story of your domain - Mads Opheim & Anne Landro = 48:10
XrKEEYzOPcw = 3 years ago = No Nonsense UI Design - Erik Engheim = 51:42
IXNIqThaSs8 = 3 years ago = Unicode - going down the rabbit hole - Peter Bindels = 56:16
U_kn8LCUjMY = 3 years ago = Customizing Qt to create first class graphical experiences on highly customized hardware = 53:35
h_5C_9hZIN0 = 3 years ago = Using Conan in a real-world complex project - Kristian Jerpetjøn = 56:37
Go1zrSvHQmA = 3 years ago = Prioritizing Security correctly - Ole Alexander Pihl Konstad = 52:26
8WTJWvR9HXg = 3 years ago = Overview on the Synthesis of Beyond Budgeting, Open Space, Sociocracy & Ag = 59:55
cotGM17my00 = 3 years ago = Locknote: The Internet of Pwned Things - Troy Hunt = 36:54
7-aXp-u6008 = 3 years ago = Compile Time Regular Expressions - Hana Dusíková = 1:03:23
ieERUEhs910 = 3 years ago = "New" Features in C - Dan Saks = 59:52
nqfgOCU_Do4 = 3 years ago = C++ Code Smells - Jason Turner = 56:11
XH4xIyS9B2I = 3 years ago = C++ Smart Pointers - Usage and Secrets - Nicolai Josuttis = 1:02:22
73nB9-HYbAI = 3 years ago = Containers unplugged: understanding user namespaces - Michael Kerrisk = 54:05
0kJPa-1FuoI = 3 years ago = Containers unplugged: Linux namespaces - Michael Kerrisk = 53:39
YUWuNpxZa5k = 3 years ago = Modern techniques for keeping your code dry - Björn Fahller = 51:26
HgmnJzDC-Nw = 3 years ago = Anchored Metadata - Austin Bingham = 55:14
lgWr0o0Wx1A = 3 years ago = "Allegro" Means Both Fast and Happy. Coincidence? - Andrei Alexandrescu = 55:14
xGJTkDb45PY = 3 years ago = Securing the Connected Car - Mirza Krak = 43:07
2j9M4frpHFg = 3 years ago = HiMake - the build tool that builds the Kongsberg missile software - Arne Førlie = 46:25
uqehwCWKVVw = 3 years ago = Developing the Bloomberg Terminal -- Local performance & measurement techniques - Paul Williams = 1:04:23
0kgTuWkyorc = 3 years ago = Storage Duration and Linkage in C and C++ - Dan Saks = 58:14
RTv_-0ITokk = 3 years ago = The Hitchhiker's Guide to Faster Builds - Viktor Kirilov = 1:00:01
hFpKOO3TxZ0 = 3 years ago = How to build Python-C++ libraries - Jørgen Kvalsvik = 48:32
Zotgrg71BIY = 3 years ago = Using Android as OS for a single purpose system - Martin Ertsås = 42:49
rhFgsrh_3r4 = 3 years ago = A Short Life span - For A Regular Mess - Victor Ciura = 56:54
B8LhQKJ7a9Y = 3 years ago = From circuit board design to finished product: the hobbyist’s guide to hardware manufacturing = 42:00
7WNI_bciFlA = 3 years ago = How did Linux become a mainstream embedded operating system? - Chris Simmonds = 43:02
xg9qofH_eDM = 3 years ago = Developing a missile simulator - Arnstein Tinjar = 49:03
hgS_xPu8DyY = 3 years ago = How I learned to love Ada as a C++ developer - Maya Posch = 1:00:24
CwCJBpB7Z5w = 3 years ago = Generators, Coroutines and Other Brain Unrolling Sweetness - Adi Shavit = 56:06
L716Ta5mzRk = 3 years ago = Model Based SW Engineering: a success story from development of the Joint Strike Missile = 54:21
jl6UkLrkkIw = 3 years ago = C++ in containers - Marc Goodner = 58:58
bWkGmRkDyt4 = 3 years ago = C++ Modules and Large-Scale Development (Part 2) - John Lakos = 1:12:40
tn0l4EQHdZA = 3 years ago = C++ Modules and Large-Scale Development (Part 1) - John Lakos = 1:01:27
ut40iShzqEY = 3 years ago = C++ Concepts for Developers - Hubert Matthews = 53:50
9zpHdh70Xdk = 3 years ago = The Most Average Function There Is - Andrei Alexandrescu = 58:56
M0qy6RiMU90 = 3 years ago = C++: λ Demystified - Andreas Fertig = 57:15
cOtb8Sb88TY = 3 years ago = Combining C++17 Features - Nicolai Josuttis = 59:22
34FLhwkrwoQ = 3 years ago = The TANDBERG Way - Olve Maudal = 1:06:59
evV1brjMuH8 = 3 years ago = NDC TechTown 2019 Keynote: Elections: Trust and Critical Infrastructure - Patricia Aas = 58:10
gvQVsFszHgc = 3 years ago = An in-flight port from Angular to React, a tale of performance and happiness - Christiansen & Paulin = 47:21
60ZS-WFiwHA = 3 years ago = NDC Sydney 2019 = 1:24
6SHc7DWDDs4 = 4 years ago = Privacy and GDPR: What all developers should know - Johannes Brodwall = 59:55
J0mcYVxJEl0 = 4 years ago = Correcting Common Async/Await Mistakes in .NET - Brandon Minnick = 1:00:11
biDJkJ4L_K8 = 4 years ago = Advanced .NET debugging techniques from real world investigations - Christophe Nasarre and Kevin Gos = 1:03:54
kIo7DNAd_oo = 4 years ago = Hack to the Future - Troy Hunt = 59:36
q9Ztb1y4Hxw = 4 years ago = A practical look at security and identity in ASP.NET Core and Entity Framework Core - Jon P Smith = 56:58
WWxpfJzv9xw = 4 years ago = Security Static Analysis - Avoiding an Angry Mob of Engineers - Josh Brown-White = 57:49
uW-Kk7Qpv5U = 4 years ago = Blazor, a new framework for browser-based .NET apps - Steve Sanderson = 59:26
ZqQ5gFB2Ty4 = 4 years ago = Best practices for securing CI/CD pipeline - Victoria Almazova = 50:00
-KwQLrwXl34 = 4 years ago = Shaving my head made me a better programmer - ​Alex Qin = 38:09
2u6q8MmyPQI = 4 years ago = UX Design Fundamentals: What do your users really see - Billy Hollis = 1:00:25
Fvu2DJU-dFg = 4 years ago = Logging, Metrics and Events in ASP NET Core - Martin Thwaites = 54:02
a3apo1ptIYY = 4 years ago = A practical guide to deep learning - Tess Ferrandez-Norlander = 1:00:49
bLN1UOT8mM0 = 4 years ago = The Moon: Gateway to the Solar System - ​Richard Campbell = 1:03:26
bkYDI-5IQdc = 4 years ago = Real world hypermedia at NRK TV - Einar W. Høst = 41:23
pvIA5wvAjAU = 4 years ago = Building a bank from scratch in the Cloud - Hans Kristian Flaatten = 56:30
Q6TOgdVgmaY = 4 years ago = Moving the enterprise to Kubernetes - Gustav Kaleta and Fredrik Klingenberg = 54:31
SrdRIHo2M3Q = 4 years ago = Powering 100+ million daily users - Rezaul Hoque = 41:57
9D0rOAWpEjs = 4 years ago = The New Frontier: A Gentle Introduction to Rust - Matthew Gathu = 1:03:49
NoGyFQ99NgY = 4 years ago = Write your own domain specific language with F# - Mikhail Smal = 43:11
4PX6yyMSnFw = 4 years ago = Functional Web Programming in .Net with the SAFE Stack - Anthony Brown = 54:25
kxq0KfVjAmg = 4 years ago = How we messed everything up but still got LoRa to the stratosphere - Sindre Lindstad = 10:07
5sbSaZ9vqTo = 4 years ago = Mobile AR in 10 minutes - Kristina Simakova = 10:43
kIhITzw0CG8 = 4 years ago = I didn't know that - Stefan Judis = 10:27
YDMAXkpzahk = 4 years ago = What's cooking for JavaScript: a look at current TC39 proposals - Branislav Jenco = 11:21
-9035dMfbRY = 4 years ago = Why our products and communities need our empathy - Sasha Romijn = 54:25
yIeNQ0iRVC4 = 4 years ago = Securing the web with AI - Callum Whyte = 48:11
ajA8gmpKLuY = 4 years ago = 5 Tips for Cultivating EQ in the Workplace - Christina Aldan = 1:03:22
WlGEOu-Ka-E = 4 years ago = Kotlin coroutines: new ways to do asynchronous programming - Svetlana Isakova = 59:05
AsSMKL5vaXw = 4 years ago = Developing Kernel Drivers with Modern C++ - Pavel Yosifovich = 1:01:31
E3dSXDNEx7c = 4 years ago = Deliberate Architecture - Robert Smallshire = 59:13
msi4WNQZyWs = 4 years ago = The Curiously Recurring Pattern of Coupled Types - Adi Shavit and Björn Fahller = 55:26
1fjGPG-v76s = 4 years ago = Life Beyond Distributed Transactions: An Apostate's Implementation - Jimmy Bogard = 52:54
64w1zbpHGTg = 4 years ago = Monolith Decomposition Patterns - Sam Newman = 1:01:08
BIrYgDHueNg = 4 years ago = Empower Your Microservices with Istio Service Mesh - Hossam Barakat = 51:45
Cis8DpUZzrM = 4 years ago = Getting Started with Cosmos DB + EF Core - Thiago Passos = 56:25
tJKXGlIhris = 4 years ago = Deep Learning in the world of little ponies - Galiya Warrier = 53:13
yOYodfN84N4 = 4 years ago = A Skeptics Guide to Graph Databases - David Bechberger = 1:00:54
5SYjR2D4p0c = 4 years ago = ML and the IoT: Living on the Edge - Brandon Satrom = 58:44
dzI7tfK0p2I = 4 years ago = Real-Time, Distributed Applications w/ Akka.NET, Kubernetes, .NET Core, and Azure Kubernetes Service = 55:42
XOvojmeT0Xk = 4 years ago = Code the future, now - Adam Ralph = 55:06
ybDD8xCqYcc = 4 years ago = Kotlin for C# Developers - Alex Dunn = 55:41
XJsgvyMm-HY = 4 years ago = Mirror mirror on the wall, what is the vainest metric of them all? - ​Paul Stack = 57:15
RprYXy5VGBc = 4 years ago = Keynote: Enterprise transformation (and you can too) - Donovan Brown = 53:08
mMzVCU38Sxo = 4 years ago = Living in eventually consistent reality - Bartosz Sypytkowski = 56:48
g1618FioGaU = 4 years ago = Is AI right for me? - Amber McKenzie = 50:05
BRLKNH6A3ds = 4 years ago = Hacking with Go - Victoria Almazova = 57:24
p2ezcieK1So = 4 years ago = The Visible Developer- Why You Shouldn't Blend In - Heather Downing = 58:46
6C-_8mjGinY = 4 years ago = Celebrate Your Expert: Overcoming Imposter Syndrome - Jay Harris = 45:07
Id2jBMJLz2Y = 4 years ago = Trying to learn C# - Patricia Aas = 56:44
E2ihHeatBCc = 4 years ago = Rediscovering fire - on designing portable, multi-language libraries - Jørgen Kvalsvik = 50:14
sn2IyBL-fbs = 4 years ago = Evolving compositional user interfaces - Thomas Presthus & Asbjørn Ulsberg = 1:03:29
Nhhm5yC2HCo = 4 years ago = It's about time - Christin Gorman = 52:18
Nl0NWh7VK8s = 4 years ago = Who's Who? Federating Identity with Azure B2C - Andrew Coates = 1:03:37
yoP2uNYFGSw = 4 years ago = Machine Learning: The Bare Math Behind Libraries - Piotr Czajka and Łukasz Gebel = 53:13
RNykMU7wF7s = 4 years ago = Protecting sensitive data in huge datasets: Cloud tools you can use - Felipe Hoffa = 46:13
4pGhvcVz1Xg = 4 years ago = ML BuzzWords demystified - Oleksandra Sopova & Natalia An = 53:26
QaMD9EIsKgQ = 4 years ago = The Hitchhiker's Guide to the Cloud - Bruno Amaro Almeida = 40:48
Ouze2uecu-o = 4 years ago = Advanced Azure App Services - K. Scott Allen = 57:50
CIDFB6XfoCg = 4 years ago = Live Site Culture & Site Reliability at Azure DevOps - Martin Hinshelwood = 1:05:03
6EV-3_m0uVk = 4 years ago = Creating solutions for everyone - Alex Mackey = 46:55
wBOHUHUq-Dw = 4 years ago = Building Great Teams - Donna Edwards = 58:09
PoFsz2xTVeo = 4 years ago = The Neverending Story: Agile Transformation for DevOps - Sarah Ziegenfuss = 46:25
STeRUhp2urA = 4 years ago = Entity Framework debugging using SQL Server: A Detective Story - Chris Woodruff = 56:23
HiIJqMqFbC0 = 4 years ago = Serverless with Knative - Mete Atamel = 57:25
3LtQWxhqjqI = 4 years ago = Architecture: The Stuff That's Hard to Change - Dylan Beattie = 45:27
NaPFclo-KbA = 4 years ago = Microservices without DDD is risky business! - Trond Hjorteland = 39:46
znYgNXN98Ag = 4 years ago = CompSci and My Day Job - Rob Conery = 52:28
JeASHwWx_QI = 4 years ago = Deep Learning in Microsoft Azure: CNTK, CaffeOnSpark and Tensorflow - Jen Stirrup = 58:09
esEDPtBJz40 = 4 years ago = System Stable: Robust connected applications with Polly, the .NET Resilience Framework - Bryan Hogan = 1:00:23
gc1AxbNybvw = 4 years ago = Lowering in C#: What's really going on in your code? - David Wengier = 56:16
uTv8K21scGQ = 4 years ago = Modern Continuous Integration with Azure Pipelines - Edward Thomson = 56:50
BL3TfA0UEr8 = 4 years ago = Dev and Test Agility for your Database with Docker - Julie Lerman = 1:07:01
ntGBRi_I3MM = 4 years ago = War stories from .NET team - Karel Zikmund = 49:11
ClPcKZHMFBg = 4 years ago = DevOps for Machine Learning - Damian Brady = 56:36
SGi1to5PP3Y = 4 years ago = Futurology for Developers - the Next 30 Years in Tech - Mark Rendle = 1:03:12
3NT7uMV8GhQ = 4 years ago = Building personalization with Orleans and Actor Modelling - Harald Schult Ulriksen = 54:05
BO-SKMS-D_g = 4 years ago = Solving Tricky Coordination Problems in Stateless .NET Services - Loris Cro = 45:41
d35nBxppmZ4 = 4 years ago = Making the most of Security Tests - Paweł Krzywicki = 50:58
ZCRYBivH9BM = 4 years ago = Fabulous – F# for cross-platform mobile apps - Don Syme = 46:22
sMI38d-mocI = 4 years ago = Security – only developers can make it proactive - Beata Szturemska = 23:30
htX0SXSTmHg = 4 years ago = Security Vulnerabilities Decomposition: Another way to look at Vulnerabilities - Katy Anton = 43:25
pP1F4b3tzsw = 4 years ago = Getting started with Azure DevOps - Donovan Brown = 1:00:09
CGD_JPnOJAg = 4 years ago = Cognitive biases in software development - Ian Hughes = 59:46
NPf88orMJT4 = 4 years ago = Source Instrumentation for Monitoring C++ in Production - Steven Simpson = 53:21
BJrQKKkooN0 = 4 years ago = 5 Lessons Learned from Implementing 40+ Machine Learning Projects - Xiaopeng Li = 14:43
hi99zbRzkRM = 4 years ago = test && commit || revert. What?! - Kari Eline Strandjord = 8:23
AqcReFElr4E = 4 years ago = Five Ways to Break a Git Repository - Edward Thomson = 13:26
rCaje8G9GeU = 4 years ago = Unlocking the doors of parliament - Sindre Lindstad = 7:50
sDRj20MWm-E = 4 years ago = How to tame your team monsters! - Hanne Lian & Nora Holte = 11:05
f_Fn_dYWAx0 = 4 years ago = I Love Learning From People! - Bryan Hogan = 13:01
E1vd3tssiss = 4 years ago = "OMG! A Girl?!" What to do when a woman joins your team - Meg Gotshall = 11:25
A1c_dIiahcU = 4 years ago = How to deal with your demons - Lubaba Farin Tanisha = 11:27
4RNlCc_l8A8 = 4 years ago = Emojis – the fun and weird parts! - Jøran Vagnby Lillesand = 12:40
w_Y6C0QgmL0 = 4 years ago = Practical Chaos Engineering  breaking things on purpose to make them more resilient against failure = 1:02:25
_lV6rXSNH-k = 4 years ago = Universal Design of Software Solutions  Necessary for some, good for everyone = 40:25
mOsiLZGdXS4 = 4 years ago = Terraform best practices with examples and arguments - Anton Babenko = 46:00
9ev4qhvLpxs = 4 years ago = Observability Driven Development - Geert van der Cruijsen = 53:17
0er3BksoJME = 4 years ago = Lessons from the API Management trenches - Eldert Grootenboer = 1:00:06
klHyc9HQnNQ = 4 years ago = Building a parser in C#, from first principles - Nicholas Blumhardt = 51:30
iGevKa6WAI8 = 4 years ago = How to be cool in the age of legacy - Jøran Vagnby Lillesand = 50:25
2kfCXMoVCqM = 4 years ago = Bulletproof Transient Error Handling with Polly - ​Carl Franklin = 41:53
24qazsRnc40 = 4 years ago = Pragmatic Performance: When to care about perf, and what to do about it - David Wengier = 56:43
jxf8uaOOu48 = 4 years ago = An Introduction to WebAssembly - Guy Royse = 59:57
x-d-qhkbDLg = 4 years ago = Build your Cloud Operating Model on Azure from zero to hero - David Pazdera = 55:10
qgZ3JO2khFg = 4 years ago = Why FIDO Security Keys & Webauthn are Awesome - Jen Tong = 46:49
5nKPEXFyFxM = 4 years ago = How to use ML NET to write crushing metal riffs - Michał Łusiak = 57:55
noUiGrbL2CM = 4 years ago = Heterogeneous pipeline processing with Kubernetes and Google Cloud Pub Sub - Håkon Åmdal = 51:53
HSTweR77nug = 4 years ago = Pointless or Pointfree - Damjan Vujnovic = 53:51
v1Elm3YlR-U = 4 years ago = The Seven Deadly Presentation Sins - Samantha Coates and Andrew Coates = 57:50
SvEj9H0ntx0 = 4 years ago = Empathetic Design Systems - Jennifer Wong = 38:29
JaMJJTb_bEE = 4 years ago = What vulnerabilities? Live hacking of containers and orchestrators - Lewis Denham-Parry = 56:41
s6rYDP1emUA = 4 years ago = Indexing and searching NuGet.org with Azure Functions and Search - Maarten Balliauw = 58:42
zOy3-_Cdhn4 = 4 years ago = Securing Web APIs from JavaScript/SPA Applications - Brock Allen = 58:47
ifuwzHQ8TeA = 4 years ago = Anchored Metadata - Austin Bingham = 46:56
wSSwuqwqNs0 = 4 years ago = Crash, Burn, Report - Scott Helme = 1:01:55
69gxtHbvZVQ = 4 years ago = We are the guardians of our future - Tess Ferrandez-Norlander = 54:23
ai0MLsoN0Gk = 4 years ago = Adding business logic to your tokens. What could possibly go wrong - Linda Lawton = 47:44
FVS1kSEr5ic = 4 years ago = Developing privacy - Glenn F. Henriksen = 52:01
rY6oo0sOMis = 4 years ago = Functional Patterns for the Object Oriented - Øystein Kolsrud = 52:14
mlVUpxXbavs = 4 years ago = Terraforming Azure - Torstein Nicolaysen = 1:02:56
bK-Tz-GLfOs = 4 years ago = The Functional Toolkit - Scott Wlaschin = 1:01:19
qEI9MOO5iFU = 4 years ago = DIY Async Message Pump: Lessons from the trenches - Daniel Marbach = 1:00:24
2wWUURZzYOo = 4 years ago = Chasing holograms - the future of HoloLens development - Scott Leaman = 1:05:18
o7R7RbPDVzY = 4 years ago = A Primer on Functional Programming - Sarah Withee = 31:09
4DI8jd7WWIQ = 4 years ago = Azure on the cheap - Karl Syvert Løland = 46:13
BdiLKxSu-2Q = 4 years ago = Understanding Git — Behind the Command Line - Enrico Campidoglio = 51:13
B_tCxLcZ4UI = 4 years ago = Getting out of quicksand, with DevOps! - Roman Pickl = 54:09
Ak_ccXFVVWw = 4 years ago = Chinafy your apps + Lessons you can steal from China - Adam Cogan = 1:10:41
0ZchSZPjsY0 = 4 years ago = Kill Evil Mutants! - Dave Aronson = 59:55
8f7bg5YAdds = 4 years ago = 10 years of microservices at FINN.no - and we still haven’t slain that dragon! - Henning Spjelkavi = 59:53
qVyPAU1Y9nk = 4 years ago = Testing GraphQL: From Zero To Hundred Percent - Roy Derks = 40:34
uuc3MjigHSg = 4 years ago = Panel discussion on the future of .NET = 1:00:58
9uzRf_t46w0 = 4 years ago = CSS Grid - What is this Magic?! - Amy Kapernick = 58:12
nH3pQbsEMzo = 4 years ago = Responsible JavaScript - Jeremy Wagner = 58:15
2-TKda71mUc = 4 years ago = Web components and micro apps, the web technologies peacekeeper - Yaser Adel Mehraban = 58:19
Xp6Kv62rlHw = 4 years ago = I'm Going To Make You Stop Hating CSS - Lemon = 47:42
hlNVXWZoP0Y = 4 years ago = Mechanical C++ Refactoring in the Present and in the Future - Stephen Kelly = 58:40
XSnzb3LaX5E = 4 years ago = Making IoT: An Intro for Web Devs - Kristina Durivage = 49:16
k7nAtrwPhR8 = 4 years ago = Rust for C++ developers - What you need to know to get rolling with crates - Pavel Yosifovich = 58:45
m6S9ZZOh0CQ = 4 years ago = C++: λ Demystified - Andreas Fertig = 1:00:06
XAZM0koJIIU = 4 years ago = Dungeons, Dragons and Functions - Mathias Brandewinder = 1:02:25
0B1U3fVCIX0 = 4 years ago = C# and Rust: combining managed and unmanaged code without sacrificing safety - Ashley Mannix = 58:01
Gu0G7ofsaoA = 4 years ago = Avoiding the Agile Alignment Trap with DevOps - Mike Long = 43:08
_d0OXm0dRZ4 = 4 years ago = Automatic text summarization - Masa Nekic = 58:06
omHp3NxKcVs = 4 years ago = Drones & AI - What's all the buzz about ? - Adam Stephensen = 57:03
CUbZ5tNZi7M = 4 years ago = Why databases cry at night? - Michael Yarichuk = 42:12
32m8luvA9Qg = 4 years ago = How to Steal an Election - Gary Short = 1:04:42
ux_9hqxiqpI = 4 years ago = An introduction to Machine Learning using LEGO - Jeppe Tornfeldt Sørensen = 57:49
QvaPka0lmdU = 4 years ago = Advanced Serverless Workflows with Durable Functions - Jeremy Likness = 57:43
PreAnSofAsA = 4 years ago = Event Driven Collaboration - Ian Cooper = 56:51
FdgTVXQQtpw = 4 years ago = Adding Observability to Distributed Systems - David Ostrovsky = 1:01:51
qtIsPSVwErQ = 4 years ago = Reactive DDD—When Concurrent Waxes Fluent - Vaughn Vernon = 58:19
3AAzySH3A88 = 4 years ago = Getting to DDD: Pragmatic or Principled? - Julie Lerman = 1:04:49
6_fSdnsjw8g = 4 years ago = Building APIs Rapidly with Azure Functions - Lars Klint = 55:05
aw1UQJcwDcc = 4 years ago = C# 8 and Beyond - Filip Ekberg = 54:15
nK54s84xRRs = 4 years ago = Writing Allocation Free Code in C# - Matt Ellis = 1:00:15
YSPiKL-bkfI = 4 years ago = Writing a Neural Net from Scratch - Joe Albahari = 56:35
6nHRk_9Lxss = 4 years ago = What is the point of Microsoft? 3.0 - Liam Westley = 57:10
xdSSH63IZZc = 4 years ago = Hidden gems in .NET Core 3 - David Fowler & Damian Edwards = 1:00:33
nTW261jbS7g = 4 years ago = Unity 101 for C# Developers - Andy Clarke = 1:00:19
ZwvpW-ldbOM = 4 years ago = Three Rewrites, One Startup - An Architect’s Journey - Spencer Schneidenbach = 1:01:14
6MJHYQ4dmAI = 4 years ago = Turing's Toy - The story of a mathematical idea that changed the world - Øystein Kolsrud = 49:45
Z0j1m7qwk3M = 4 years ago = Code Review Etiquettes 101 - Janani Subbiah = 34:00
e7K0dsQpjuE = 4 years ago = I thought we did things right until I went looking - Security errors in Norwegian websites - Håvard = 9:06
a7GLQdy2nnM = 4 years ago = RSA encryption in 10 minutes - Fredrik Meyer = 15:25
GokBv-NWsFw = 4 years ago = What hit my webservice with 408?! - Paweł Krzywicki = 11:50
inX3gxeKH0o = 4 years ago = Root-of-trust - What it is and why you need one in IoT - Ole Alexander Konstad = 9:50
C0PWEq_F2OA = 4 years ago = IoT meets IPv6: The Perfect Storm? - Kristian Bognæs = 9:06
O6IrIHO1yR4 = 4 years ago = Shiny objects are cool, but so is building products people use - Jenna Pederson = 54:55
SvN-otkzXeM = 4 years ago = DevOps ICU: Improving DevOps Results by (Correctly) Integrating UX - Debbie Levitt = 1:01:09
BCyHS7s_pjc = 4 years ago = Keynote: Leadership Guide for the Reluctant Leader - David Neal = 40:01
FH-RZiOq4h0 = 4 years ago = The Shape of Data: Machine Learning and Topology - Kaisa Taipale = 49:30
i3RXbOY6-0I = 4 years ago = SignalR: To Chat and Beyond - David Pine = 52:52
4yALYEINbyI = 4 years ago = Patterns for high-performance C# - Federico Andres Lois = 1:08:55
ufWqhtolikg = 4 years ago = One Codebase to Rule Them All - Using React Native Everywhere - Jesse Weigel = 58:43
BvVNGTAbPss = 4 years ago = How not to be the best app no one uses: Effective Onboarding for fun & profit - Kendall Miller = 1:01:25
Pgx1wzMVLyw = 4 years ago = Azure Functions 2.0: Enterprise-Grade Serverless - Katy Shimizu = 47:44
gT7H0qBdQq8 = 4 years ago = CSS Grid - What is this Magic?! - Amy Kapernick = 51:49
FL1lHaY1tG8 = 4 years ago = From one release per quarter to 30 times a day - Marcel de Vries = 1:00:48
ev5k51AxZbI = 4 years ago = The Dark Side Of Events - Vladik Khononov = 59:05
sPnx7EkALuQ = 4 years ago = HACKERS, HOOLIGANS, HEISTS, & HISTORY - Brian Contos = 59:08
jqBkWc42-BQ = 4 years ago = Networking at conferences for autistic people and introverts - Dennie Declercq = 55:29
Ku0lD3-e9oA = 4 years ago = Scaling microservices with Message queues, .NET and Kubernetes - Lewis Denham-Parry = 41:38
RGzLhwkekDk = 4 years ago = UX Design Fundamentals: What do your users really see - Billy Hollis = 1:00:51
YOlbtNgrgBE = 4 years ago = IP Fundamentals—Trust Me, I'm a Lawyer - Jeff Strauss = 1:02:00
vu0ryDBAIq4 = 4 years ago = Quantum Computing Concepts - John Azariah = 1:01:15
VuR4UaV7Q0k = 4 years ago = Continuous Learning for Developers - Brian MacDonald = 52:25
DwaV5RcTdOs = 4 years ago = Cypress: Where Automated Acceptance Testing Isn’t Just for QA Anymore - Justin James = 55:36
j6f3NSfDPoE = 4 years ago = Modern web application bugs - Erlend Oftedal = 57:32
mFG-S8I929U = 4 years ago = DevOps for Machine Learning - Damian Brady = 55:41
P7h1rssb9eg = 4 years ago = Service Workers: Transforming your App into a Progressive Web Application - Avindra Fernando = 1:02:18
3HidYKjiAqQ = 4 years ago = Life Beyond Distributed Transactions: An Apostate's Implementation - Jimmy Bogard = 59:56
_Sx4Od71BYU = 4 years ago = Game On! Gamifying Your Apps for Fun and Profit - Gwendolyn Faraday = 56:49
Ptnxc6tVIPE = 4 years ago = Using C# Expression Trees in the Real World - Spencer Schneidenbach = 50:56
Bf6qXG2TkH8 = 4 years ago = CloudWatch-ing: Creating More Useful Logs & Alerts with AWS - Rhia Dixon = 42:17
7lOKh6g-1dQ = 4 years ago = Bulletproof Transient Error Handling with Polly - Carl Franklin = 50:55
SHPRDB76ymI = 4 years ago = Distributed Tracing and Monitoring with OpenCensus - Simon Zeltser = 59:12
YRwAgOiGS_s = 4 years ago = Dungeons, Dragons and Functions - Mathias Brandewinder = 1:00:46
8De8DlrCzoY = 4 years ago = Blazor: C# running in the browser via WebAssembly - Scott Sauber = 57:50
F0hAZC2LTcI = 4 years ago = Goodbye REST APIs. Hello GraphQL! - Cory House = 1:01:57
MSWPYhqSbW8 = 4 years ago = How to Build a RESTful Service with ASP.NET Core and Swagger - Gregor Dzierzon = 57:11
vx6O8w-5_VQ = 4 years ago = Getting Started with Cosmos DB + EF Core - Thiago Passos = 45:13
RQve_bD8X_M = 4 years ago = Clean Architecture with ASP.NET Core 2.2 - Jason Taylor = 50:36
0_6pSLVkaMM = 4 years ago = An AI with an Agenda: How Our Cognitive Biases Leak Into Machine Learning - Arthur Doler = 56:03
T42dnlzSNE8 = 4 years ago = Hacking Humans : Social Engineering Techniques and How to Protect Against Them - Stephen Haunts = 49:36
HqImpLBJTeA = 4 years ago = Serverless with Knative - Mete Atamel = 47:18
nNhL5UluNtA = 4 years ago = UX + Engineering: A Tale of Two Cities - Edward Ecker & Joe Karlsson = 50:30
Z9MN01qDJyQ = 4 years ago = Hacking Your Processes - Richard Wellum = 50:37
68OvQtsCjlA = 4 years ago = Everyday Agile for One: Recipes that make development for one … Fun - Elsa Vezino = 46:42
qdXZwmn7oLY = 4 years ago = NDC Porto 2020 - Save the date! = 1:01
pKN7Yoamx74 = 4 years ago = Are You Really Using Kanban, or Just Making a List of Issues? - Tom Cudd = 48:22
wMa34PhY4F0 = 4 years ago = Augmented Reality - The State of Play - Rafał Legiędź = 55:51
PrYJQ1EqfTg = 4 years ago = Securing Web Applications and APIs with ASP.NET Core 2.2 and 3.0 - Brock Allen = 1:03:06
c0LcuPRBFvo = 4 years ago = Modern Web Testing: Going Beyond Selenium - Dmitry Vinnik = 54:57
cAVvV0_aIwI = 4 years ago = Fundamentals of Azure IoT - Justin Grammens = 1:03:47
zeMEKwsK7fI = 4 years ago = How to Escape The Distributed Monolith - Ian Cooper = 59:25
o9qL4HcDpIQ = 4 years ago = Async injection - Mark Seemann = 1:01:01
K003tt9_khA = 4 years ago = No Strings Attached: JavaScript without Webpack, Transpilers, or Frameworks - Ashley Grant = 59:27
wTvisUbU9FU = 4 years ago = Exploring C# 8: The Deep Dive - David Pine = 47:29
iB-g3AGwZIo = 4 years ago = ECMA 6 JavaScript, the Good Parts - Jennifer Estrada = 50:46
mIejhIX7ObE = 4 years ago = Designing a Flexible UI Architecture with React and GraphQL - Kamran Ayub = 1:02:13
GGF_QiGkOtY = 4 years ago = A Skeptics guide to functional style javascript - Jonathan Mills = 49:01
D4_1LU9jljk = 4 years ago = From zero to CD in 60 minutes - Glenn F. Henriksen = 1:04:35
q5A0Hd7fO8g = 4 years ago = From localhost to production: Managing your code with Azure DevOps -  Jay Harris = 1:08:45
FVerD7y4DSc = 4 years ago = Kubernetes - going beyond the basics - Shahid Iqbal = 59:28
W0Jc_Oh7r58 = 4 years ago = Kubernetes, Azure and .NET - What's it all about? - Shahid Iqbal = 1:01:26
PQGlhbf7o7c = 4 years ago = Elasticsearch Suggesters: Beyond Autocomplete - Brett Hazen = 50:00
od4mrgJ9wW8 = 4 years ago = Serverless Architecture Patterns - Lynn Langit = 1:01:59
qCOefMiakps = 4 years ago = Keynote: Hack to the Future - Troy Hunt = 55:20
0TYbHVc2yWI = 4 years ago = Autonomous microservices don't share data. Period - Dennis van der Stelt = 47:11
w7MqXRLHnt8 = 4 years ago = Real World Guide to Web API authentication on Azure - Heather Downing = 54:36
_jA4gLZtFSE = 4 years ago = Keyboards? Where we’re going, we don’t need keyboards - Don Wibier = 51:00
nFw23In-BtI = 4 years ago = Reading other peoples code - Patricia Aas = 55:38
miXZNvGp2uY = 4 years ago = Protecting Encryption Keys with Azure Key Vault - Stephen Haunts = 1:03:20
hev65ozmYPI = 4 years ago = All our aggregates are wrong - Mauro Servienti = 58:04
LY8F2g6vrnM = 4 years ago = Quantum Computing Concepts - John Azariah = 1:01:40
PHDct6oIneE = 4 years ago = Dungeons, Dragons and Functions - Mathias Brandewinder = 58:56
bAfVasWqnsY = 4 years ago = Developer Accessible Machine Learning - Michal Lusiak = 42:41
8ism68urcAM = 4 years ago = Recent Solutions Using Deep Learning Models/ The How and Why - Hazel Clarke = 36:58
xjf3eW5lftw = 4 years ago = Agility ≠ Speed - Kevlin Henney = 1:03:25
ZtA5GmxVQEo = 4 years ago = Fantastic Mr. Function - Damjan Vujnovic = 1:02:32
EN-ny9Qw9HE = 4 years ago = A Practical Guide to Dashboarding - Jessica White = 49:14
YF8coyfQb0Y = 4 years ago = Building Clients for OpenID Connect/OAuth 2-based Systems - Dominick Baier = 1:00:31
9x44KwmElko = 4 years ago = Code the future, now - Adam Ralph = 54:31
VvJvQvzqKIU = 4 years ago = Securing Web Applications and APIs with ASP.NET Core 2.2 and 3.0 - Dominick Baier = 52:05
NbeZ8clZtb4 = 4 years ago = What Is This Cloud Native Thing Anyway? - Sam Newman = 51:25
bVlWWCru-28 = 4 years ago = Async injection - Mark Seemann = 1:00:30
N78NxZ-cKUc = 4 years ago = A lap around Azure Devops - Jakob Ehn = 1:02:59
3g96lmsWs-M = 4 years ago = CSS Grid - What is this Magic?! - Amy Kapernick = 44:51
EBe0k7na1FQ = 4 years ago = Pragmatic Performance: When to care about perf, and what to do about it - David Wengier = 54:04
wPlfHrdjMMA = 4 years ago = Dynamic Runtime Code with Roslyn - Jeremy Miller = 1:01:21
Pmm12LtcPWs = 4 years ago = GraphQL Will Do To REST What JSON Did To XML - Roy Derks = 32:43
g2cu7xmX-98 = 4 years ago = A Skeptic's Guide to Functional Style Javascript - Jonathan Mills = 47:54
YpY45Dn0fNw = 4 years ago = Deep Learning in the world of little ponies - Galiya Warrier = 55:01
hfwGymdqgKk = 4 years ago = Tabs, spaces and salaries: a data science detective story - Evelina Gabasova = 45:17
TuZZIGSbFfQ = 4 years ago = Architectural patterns for the cloud - Mahesh Krishnan = 1:03:28
0TKSLrN8u0E = 4 years ago = APIs Exposed! - Layla Porter = 47:08
bwSNyA1Nfz4 = 4 years ago = From 'dotnet run' to 'Hello World!' - Matt Warren = 1:04:41
MTkErReN-PQ = 4 years ago = Dungeons, Dragons and Functions - Mathias Brandewinder = 1:01:35
Hm4EDPNXQqY = 4 years ago = Build cross-platform mobile apps using Fabulous - Jim Bennett = 56:36
z4bltRpRoGg = 4 years ago = Zero to Mobile Hero - Intro to Xamarin and Visual Studio Team Services - Luce Carter = 1:02:59
09GtrS3qyZU = 4 years ago = Let’s Talk About Mental Health - Arthur Doler = 1:06:08
deHM34b21v4 = 4 years ago = Skip the first three months of development for your next app - Gojko Adzic = 56:23
cFZglw5IUsA = 4 years ago = Serverless with Knative - Mete Atamel = 52:12
hHzQKGnvYp8 = 4 years ago = ASP.NET Core: The One Hour Makeover - Jon Galloway = 1:03:13
gET51_C3k5s = 4 years ago = Patterns for Resilient Architecture - Adrian Hornsby = 1:03:09
6m9WV5uqORQ = 4 years ago = DevSecOps for Developers: How To Start - Patricia Aas = 1:02:26
IrQh6GqQt-Y = 4 years ago = Linux Security APIs and the Chromium Sandbox - Patricia Aas = 54:46
RVDIdNcLQQQ = 4 years ago = Implement DevSecOps in Azure - Victoria Almazova = 54:10
Sx2luXC3kSU = 4 years ago = Securing Kubernetes with Istio - Erlend Oftedal = 48:06
m01fqeClljI = 4 years ago = Protecting Encryption Keys with Azure Key Vault - Stephen Haunts = 56:02
jq0AcfhUba8 = 4 years ago = Building Clients for OpenID Connect/OAuth 2-based Systems - Dominick Baier = 1:01:49
YC16sMshipI = 4 years ago = Hacking a Cat — Going Beyond Traditional Attack Vectors - Niall Merrigan = 46:47
O2tZ5vmDtQs = 4 years ago = Crash, Burn, Report - Scott Helme = 1:00:28
O4BOU6JWLaQ = 4 years ago = Securing Web Applications and APIs with ASP.NET Core 2.2 and 3.0 - Dominick Baier = 1:00:30
IzTvlIqv0A4 = 4 years ago = Hack to the Future - Troy Hunt = 1:00:52
JvCyKxA5S0I = 4 years ago = Domain-Driven Design: Hidden Lessons from the Big Blue Book - Nick Tune = 37:56
M_94pyFC-Ok = 4 years ago = Icons and the Web: Symbols of the Modern Age - Tim G. Thomas = 56:14
hsJORkgMHJk = 4 years ago = Distributed Tracing: How the Pros Debug Concurrent and Distributed Systems - Aaron Stannard = 56:36
WSO9YFi6Oqs = 4 years ago = Observability and the Development Process - Christine Yen = 50:00
mRwHZTNGdoY = 4 years ago = Four Languages from Forty Years Ago - Scott Wlaschin = 1:04:41
7bJVjPrxge4 = 4 years ago = Crash, Burn, Report - Scott Helme = 58:51
1vD2fSc-Jqc = 4 years ago = Society (n+1).0: smashing the patriarchy and other ways of changing the world = 59:42
Nrp_LZ-XGsY = 4 years ago = The Functional Programmer's Toolkit - Scott Wlaschin = 1:05:51
wPjHuvulivM = 4 years ago = Ctrl-Alt-Del: Learning to Love Legacy Code - Dylan Beattie = 56:47
fWtDE34tOzg = 4 years ago = .NET Rocks Live on Software Feature Selection with Christine Yen = 49:59
LcPBhmjT2aw = 4 years ago = A practical guide to deep learning - Tess Ferrandez-Norlander = 1:00:49
si44LvcgXwU = 4 years ago = Scaling microservices with Message queues, .NET and Kubernetes - Lewis Denham-Parry = 39:49
A5z2rWdnz_o = 4 years ago = Small Steps, Giant Leaps: Engineering Lessons from Apollo - Dylan Beattie, Kevlin Henney = 1:07:30
c-plH9gG0zk = 4 years ago = The State of C# - What Have I Missed? - Filip Ekberg = 1:06:01
tWn8RA_DEic = 4 years ago = Structure and Interpretation of Test Cases - Kevlin Henney = 1:08:13
mtlK2gA4WbM = 4 years ago = CompSci and My Day Job - Rob Conery = 50:16
2yxV-I6DKGc = 4 years ago = Panel discussion on the future of .NET = 1:14:50
ejJXWAkB_2I = 4 years ago = Avoiding the Agile Alignment Trap with DevOps - Mike Long = 56:44
eut32bbozFg = 4 years ago = Getting Started with Cosmos DB + EF Core - Thiago Passos = 55:43
mK_yBTfvvN4 = 4 years ago = Building Clients for OpenID Connect/OAuth 2-based Systems - Dominick Baier = 1:00:23
_GF9GtyBQsA = 4 years ago = Securing Web Applications and APIs with ASP.NET Core 2.2 and 3.0 - Dominick Baier = 53:33
HAFKHRL4Jys = 4 years ago = What you need to know about ASP.NET Core 2.2 - Damian Edwards, David Fowler = 1:02:31
HUN1j9G1Py8 = 4 years ago = Keynote: The Microsoft Open Source Cinematic Universe - Phase 2 - Scott Hanselman = 55:59
BncBqBye_gI = 4 years ago = Futurology for Dummies - the Next 30 Years in Tech - Mark Rendle = 1:04:13
lw3HTm5EYuk = 4 years ago = The promise of an async future awaits - Bill Wagner = 1:01:04
kv2S2f_C37A = 4 years ago = Solving Diabetes with an Open Source Artificial Pancreas - Scott Hanselman = 59:27
QA1RvnXKKdY = 4 years ago = Versioning 1.0.1 - Jon Skeet = 1:00:05
BsavoQWAVqM = 4 years ago = Async injection - Mark Seemann = 58:08
SWX5yvyqRf0 = 4 years ago = Data on the Inside, Data on the Outside - Ian Cooper = 1:06:06
g3SZxsskZE0 = 4 years ago = DiagnosticSourcery 101 - Mark Rendle = 1:04:32
OPAdKv4GF-I = 4 years ago = Where is C# headed? - Mads Torgersen, Jon Skeet = 1:03:25
0RfUPr0KrSM = 4 years ago = Blazor, a new framework for browser-based .NET apps- Steve Sanderson = 1:00:45
_P1ZdVV_yic = 4 years ago = Beyond Developer - Dan North = 43:13
-I8QHkZreyo = 4 years ago = Leadership Guide for the Reluctant Leader - David Neal = 46:07
3JCvW7OSfUc = 4 years ago = How We Got Here - The History of Web Development - Richard Campbell = 1:01:25
EFraD678ro0 = 4 years ago = Hack to the Future - Troy Hunt = 1:09:40
AUrKofVRHV4 = 4 years ago = Life Beyond Distributed Transactions: An Apostate's Implementation - Jimmy Bogard = 1:01:40
J-xqz_ZM9Wg = 4 years ago = Why your ASP.NET Core application won't scale - Damian Edwards, David Fowler = 1:01:00
MdiUlmDwqEw = 4 years ago = Insecure Transit - Microservice Security - Sam Newman = 1:00:06
TOWN1zwFpo0 = 4 years ago = Real Quantum Computing - James Birnie = 1:02:57
eRz3xjM08l0 = 4 years ago = Migrating to Microservice Databases: From Relational Monolith to Distributed Data - Edson Yanaga = 1:04:52
Sv_JKGVosr4 = 4 years ago = Breaking Down Your Build: Architectural Patterns For A More Efficient Pipeline - Abraham Marin-Perez = 54:24
ZKchdjFSgbM = 4 years ago = Using Service Meshes and Kubernetes to Solve Service-to-Service Communications... - Ben Hall = 58:21
sLIqdigpFj8 = 4 years ago = Build software like a bag of marbles, not a castle of LEGO® - Hannes Lowette = 58:01
gPrCvH6bDic = 4 years ago = Building Progressive Web Apps with React - Jonathan Mills = 59:37
3YCIw3gewFE = 4 years ago = Agile Software Architecture - Ian Cooper = 1:08:52
H0DeuoIbyrs = 4 years ago = Manual memory management in .NET Framework - Adam Furmanek = 57:59
oAf3_8k17E8 = 4 years ago = HTTPS in ASP.NET Core 2 in Docker Linux Containers Deep Dive - Rob Richardson = 1:02:01
YJgBAiPlG3k = 4 years ago = Measure All The Things with App Metrics - Mark Rendle = 1:03:22
tUsbF6SuTZY = 4 years ago = Need for speed 8, performance tuning of your web application - Yaser Adel Mehraban = 1:04:07
28HTF3Ql-OM = 4 years ago = Give it a REST - Tips for designing and consuming public API's - Liam Westley = 57:00
tnwKa8j-LOU = 4 years ago = Leadership Guide for the Reluctant Leader - David Neal = 59:14
NLYpUN-oItY = 4 years ago = Handy Tools for Designing Great Web APIs - Mike Amundsen = 58:46
gWYxjfJFIoU = 4 years ago = Drones, AI & IOT - What's all the buzz about ? - Adam Stephensen = 59:38
sfLo_5mu-tQ = 4 years ago = Dungeons, Dragons and Functions - Mathias Brandewinder = 1:01:16
n-3g4qjQ0Qg = 4 years ago = A Practical Guide to Dashboarding - Jessica White = 45:29
RuVgGUk9-R0 = 4 years ago = Tabs, spaces and salaries: a data science detective story - Evelina Gabasova = 52:14
jQ1w4hIgI-A = 4 years ago = The Web That Never Was - Dylan Beattie = 58:50
YgJ5s8orUJ0 = 4 years ago = Reactive DDD—When Concurrent Waxes Fluent - Vaughn Vernon = 1:00:20
U2tivS4uCfs = 4 years ago = Build vs Buy: Software Systems at Jurassic Park - Todd Gardner = 47:03
DA6kRZ9SVTU = 4 years ago = Containers for Real Integration Tests - Philipp Krenn = 48:27
nEuYJ9bjrPA = 4 years ago = Kubernetes - going beyond the basics - Shahid Iqbal = 52:13
Lv41iZIXcbc = 4 years ago = How to seamlessly transition from Developer to Leader - Ian Hughes & Donna Edwards = 57:51
BJc3d16thLs = 4 years ago = Natural Language Processing with Deep Learning and TensorFlow - Barbara Fusinska = 54:17
jdliXz70NtM = 4 years ago = Finding your service boundaries - a practical guide - Adam Ralph = 57:53
8LA060frXZ8 = 4 years ago = .NET Rocks Live with Domnick Baier and Brock Allen = 50:27
FcFp8aghwWI = 4 years ago = ARMGDN - Build modern web apps using Apollo, React, MobX GraphQL, Db and Node.js - Vladimir Novick = 51:59
D-6CzdNCLtQ = 4 years ago = Rock-Solid Components with TypeScript and GraphQL - Mat Warger = 46:43
DP192Vmc_b0 = 4 years ago = Adapting ASP.NET Core MVC to your needs - Filip W = 1:02:10
VvUdvte1V3s = 4 years ago = Six Little Lines of Fail - Jimmy Bogard = 57:54
LvIPUZn2Rmk = 4 years ago = Neural Networks: A Primer - Rishal Hurbans = 1:02:05
9OuqyVYsUuA = 4 years ago = Practical Security for Web Applications - Chris Holland = 59:17
bYKmq_sTsRw = 4 years ago = The Enterprise DevOps Challenge - Roy Osherove = 1:02:18
zS5GLpgWNKQ = 4 years ago = Using Kotlin Coroutines for Asynchronous and Concurrent Programming - Pedro Felix = 1:02:57
V6MzzmJ9IPs = 4 years ago = The secret unit testing tools no one ever told you about - Dror Helper = 52:31
YEKFyscVSe4 = 4 years ago = Functional-first programming with F# - Tomas Petricek = 1:00:26
frfz2_9EuGA = 4 years ago = Implement DevSecOps in Azure - Victoria Almazova = 52:14
BM091_OlX3o = 4 years ago = Building Clients for OpenID Connect/OAuth 2-based Systems - Brock Allen & Dominick Baier = 57:07
s9kTKTcR1RY = 4 years ago = Scaling Frontend Development - Luis Vieira = 38:45
o0SHFJDMpgc = 4 years ago = How to build a social network entirely on serverless - Yan Cui = 43:40
qqrzEC1Eov4 = 4 years ago = C# 8 and Beyond - Filip Ekberg = 1:00:03
-ifCEO_RZJI = 4 years ago = Hacking your work life __ balance to take over the world - Jennifer Wadella = 52:48
ylaxq4koAkU = 4 years ago = Using C# Expression Trees in the Real World - Spencer Schneidenbach = 50:57
gBfV4jb1HqU = 4 years ago = Async injection - Mark Seemann = 1:02:14
TdRBUb4payY = 4 years ago = Embracing Messaging and Eventual Consistency in your Microservices Solutions - Michele Bustamante = 1:11:08
EYk3KTwwbFA = 4 years ago = Securing Web Applications and APIs with ASP.NET Core 2.2 and 3.0 - Brock Allen & Dominick Baier = 53:21
AN4RLVhwJUA = 4 years ago = Insecure Transit - Microservice Security - Sam Newman = 58:59
WHb-lJbID-4 = 4 years ago = Keynote: The Moon: Gateway to the Solar System - Richard Campbell = 54:19
l52_sTL4VQs = 4 years ago = Distributed Tracing and Monitoring with OpenCensus - Simon Zeltser = 1:01:34
Ri4uVvxiBD8 = 4 years ago = 3D printed Bionic Hand a little IOT and a Xamarin Mobile App - Clifford Agius = 1:05:33
VQFWLc6cjns = 4 years ago = What is this Blazor thing, anyway? - John Stovin = 14:34
hvzsxjVHEg8 = 4 years ago = Security stand-up - Victoria Almazova = 10:46
3yxiDDk_uqI = 4 years ago = Raising next generation of passionate coders - Tomasz Bartoszewski = 12:11
zn1IF45etT8 = 4 years ago = Poetry in the air - Suzie Gray = 10:22
KP8R2EXudg4 = 4 years ago = Read and write considered harmful - Hubert Matthews = 56:39
ATnk1wGC4tY = 4 years ago = Fallacies of Doom - Lessons learned from porting Doom 3 to Java - Mahmoud Abdelghany = 1:03:53
Zygw4UAxCdg = 4 years ago = Clean Architecture with ASP.NET Core 2.2 - Jason Taylor = 50:27
F8-V3UbCcK4 = 4 years ago = System Stable : Robust connected applications with Polly - Bryan Hogan = 55:38
ZLwggeygWho = 4 years ago = Accessible App Design - Dennie Declercq = 50:21
CZvMkXWJ0r4 = 4 years ago = I love learning from people! - Bryan Hogan = 12:21
goMYmopiCJ4 = 4 years ago = Functional Web Programming in .Net with the SAFE Stack - Anthony Brown = 1:05:00
5hjpxa52PPc = 4 years ago = How thanking people can lead to a better culture - Jim Bennett = 12:36
lKUPzXQWYq8 = 4 years ago = Help! My co-worker is autistic !? - Dennie Declercq = 11:28
NnyvqjVfMD4 = 4 years ago = Why should you care about edge computing? - Glenn F. Henriksen = 56:42
2XVoy2ZDpnI = 4 years ago = A Practical Guide to Dashboarding - Jessica White = 53:48
0U0CFipmlAc = 4 years ago = NDC MINNESOTA 2019  - Conference for Software Developers = 0:33
woBdvTd1wz4 = 4 years ago = Learn / Share / Repeat - Lewis Denham-Parry = 17:32
u0WSY0pGSfY = 4 years ago = Can a robot code my website? - Salman Iqbal = 11:28
XPs5WGCgK_I = 4 years ago = Alternative Ways To Think About Serverless - Chris Priest = 14:44
S1ldaxeznRE = 4 years ago = How My Dad Taught Me to Code - Ari Hunt & Troy Hunt = 15:41
xnYFV00_btU = 4 years ago = Reading other peoples code - Patricia Aas = 52:10
pR8zPYlNU0k = 4 years ago = Kotlin for C# Developers - Alex Dunn = 59:06
D7SbjFdEIhc = 4 years ago = Unity 101 for C# Developers - Andy Clarke = 1:02:41
CByeftIYFUY = 4 years ago = Kubernetes - going beyond the basics - Shahid Iqbal = 50:04
fki4nIvYJcc = 4 years ago = Just what is a "service mesh", and if I get one will it make everything OK? - Elton Stoneman = 1:03:15
TCfsoLcc4EQ = 4 years ago = Lessons learned building ASP.NET Core MVC - Ryan Nowak = 1:00:48
myvPCxffAlY = 4 years ago = Scaling Frontend Development - Luis Vieira = 39:55
C4fxz0004Nc = 4 years ago = An Introduction to WebAssembly - Guy Royse = 59:09
e6idWxzGiKE = 4 years ago = (WPF + WinForms) * .NET Core = Modern Desktop - Oren Novotny = 56:56
RpS0PRYnD5E = 4 years ago = Think Like a Trainer: Improving Your Communication Skills - Olivia Liddell = 58:27
kwpDed1ScvA = 4 years ago = Keeping it DRYer with Templates - Layla Porter = 44:50
SnQ1Vb4fFsk = 4 years ago = Introducing Razor Components in ASP.NET Core 3.0 - Daniel Roth = 1:02:30
-hqny1D4reI = 4 years ago = Let’s talk patterns - Chris Klug = 1:01:05
wjcuhMXuULY = 4 years ago = Build vs Buy: Software Systems at Jurassic Park - Todd Gardner = 48:32
YgI8YLr6Nz0 = 4 years ago = The tech future is diverse - Tannaz N. Roshandel & Line Moseng = 47:19
JucDGwPBuQw = 4 years ago = Power BI for Developers - Laurent Amar & Peter Myers = 57:43
BJGmkJEltC4 = 4 years ago = Designing Nullable Reference Types in F# - Phillip Carter = 53:57
IUAmowond7w = 4 years ago = Teaching New Tricks – How to enhance the skills of experienced developers -  Clare Sudbery = 1:06:28
XFuGt9HAAKo = 4 years ago = What You Need to Know About Open Source—Trust Me, I'm a Lawyer - Jeff Strauss = 57:13
VxmL6g9uy-A = 4 years ago = A Piece of Git - Edward Thomson = 56:57
0Rnjq20fhUc = 4 years ago = Megahertz, Gigahertz, Registers and Instructions: How does a CPU actually work? - Kendall Miller = 1:05:23
f7rXp0RQdpg = 4 years ago = "Hey Mycroft": Getting Started with the OSS Home Assistant - Sarah Withee = 41:26
f1xgfneVQ9Q = 4 years ago = A Developer's Guide to Advertising - Krista LaFentres = 37:14
DHPX2ShCxBc = 4 years ago = Making Accessibility Testing Suck Less: An Intro to Pa11y - Jennifer Wadella = 45:36
ojDxK_-I-To = 4 years ago = Let's Talk HTTP in .NET Core - Steve Gordon = 58:52
-IEvDBJ6D9Y = 4 years ago = Reverse Engineering a Bluetooth Lightbulb - Jesse Phelps = 52:18
zy7Y9CHji2k = 4 years ago = ML.NET for developers without any AI experience - Lee Mallon = 45:52
D2_ts6Y5UyE = 4 years ago = Build Nodejs APIs using Serverless on Azure - Simona Cotin = 58:10
PUdoCCUalUU = 4 years ago = Augmented Reality - The State of Play - Rafał Legiędź = 45:44
_ZIRYeWEzU4 = 4 years ago = Hacking with Go - Victoria Almazova = 59:26
a7mGfacGbE0 = 4 years ago = Deep Learning with PyTorch - Seth Juarez = 1:04:41
lVDYwA-BcwE = 4 years ago = Much Ado about Nothing: A C# play in two acts. Act 2 - Mads Torgersen & Bill Wagner = 1:05:23
GusJQNjj_2g = 4 years ago = Much Ado about Nothing: A C# play in two acts - Act 1- Mads Torgersen & Bill Wagner = 59:27
b32aWD5FL3Q = 4 years ago = Keynote: Welcome to the Machine - Hadi Hariri = 1:07:25
LbXtBa8wGwE = 4 years ago = NDC Security Australia 2019 Promo = 1:05
n5opi4NseO8 = 4 years ago = NDC Sydney 2019 Promo = 0:33
tjDv9Y7NYPA = 4 years ago = NDC Security Workshop: Hack Yourself First: How to go on the Cyber-Offence - Troy Hunt = 1:01
RzzUa1sIwaQ = 4 years ago = NDC Sydney 2019 = 2:14
b87sBVVW7zY = 4 years ago = Planet scale or planet fail? - Paul Gavich = 59:03
lZZabbxxttI = 4 years ago = How did our DevOps team become another silo? - Kevin Crawley = 39:37
agWbzmZvQxM = 4 years ago = The Boring Security Talk - Kieran Jacobsen = 1:02:08
riJo71GqyP4 = 4 years ago = Make Your Life Easier With Logic Apps + Save $$$ - Thiago Passos = 42:58
rSY-zqDfc_s = 4 years ago = Advanced Testing Techniques: Tips from the trenches - Graeme Foster & Rob Moore = 57:29
MiM3PXp-OrA = 4 years ago = Enterprise Mobile DevOps - Ian Hughes = 1:01:25
ZwwaBnJs4Yc = 4 years ago = Infrastructure as Code with Terraform on Azure - Tom Harvey = 47:52
ebGGqfeU08c = 4 years ago = Redux for Angular -- Introduction to Ngrx Ecosystem - Mohamed Meligy = 1:03:47
4jdW4lGiN4c = 4 years ago = This Startup Life: A Developer's Mistakes and Tips - Ben Cull = 56:05
ORC2N3oHs7U = 4 years ago = Introducing Juvet: Building Bots in Elixir - Jamie Wright = 52:25
7AztKZuMpNA = 4 years ago = Two platforms, one codebase: Cross-platform React and React Native app at Sportsbet - Ben Teese = 53:21
iIVXfHGe7rA = 4 years ago = Let's Launch A Website, Right Friggin' Now! - Lemon = 45:04
rjDvSVKH9uY = 4 years ago = Going Full Duplex - Building Apps for Speech - Madoka Chiyoda & Vishesh Oberoi = 52:14
9iKCUqLqCl8 = 4 years ago = Lightning Talks - Day 3 NDC - Sydney 2018 = 56:33
q5NGpg1No_s = 4 years ago = Implementing Augmented Reality (AR) in Apple's ARKit - Michael Ridland = 58:12
vymRRF-dSg0 = 4 years ago = Maximal Fun Times: Monitoring Theme Parks (and distributed systems) - Mike Minutillo = 43:51
CQ_Mghk2NBY = 4 years ago = Securing your dependencies - Nina Juliadotter = 40:05
rBwsrLFBg5Y = 4 years ago = Pragmatic Performance: When to care about perf, and what to do about it. - David Wengier = 43:22
gzxrnbNmtjo = 4 years ago = Deploy microservices confidently using Consumer Driven Contracts - Henrik Stene = 44:50
KIR0ftm-HNc = 4 years ago = Why Vue.js is Taking Over the Front-end World - Gwendolyn Faraday = 52:13
cCwVeRNp2S0 = 4 years ago = Crafting compelling real-time web experiences with GraphQL and React - Rob Crowley = 57:56
axbCtXG3awA = 4 years ago = Getting the first PR into .NET and other tales from an OSS contributor - Adam Ralph = 56:35
01otPuAPOJo = 4 years ago = There are no snow days when you work remote - Jennifer Wadella = 53:18
Vjscmt4eQdY = 4 years ago = A World Without Programmers? - Ravi Gadhia = 54:25
_-0GsmNIkeE = 4 years ago = Artificial Intelligence. Our journey towards singularity - Agustinus Nalwan = 47:58
R9g9gg9-Qeo = 4 years ago = Powering 100+ million daily users - Rezaul Hoque = 52:50
7jPDnF5bXNw = 4 years ago = Creating & Maintaining Impactful Dashboards' - Jessica White = 45:26
TkBOozeNtiM = 4 years ago = Haskell - A Peek Inside the Ivory Tower - Daniel Chambers = 1:04:23
bUTBBS1TECc = 4 years ago = DevOps for Data Science - Damian Brady = 58:33
m8awjR7PjZw = 4 years ago = Apps are Making Us Dumber - Heather Wilde = 47:50
tqFqN8A7waQ = 4 years ago = Modern web application bugs - Erlend Oftedal = 42:25
i5ChOMRKIoY = 4 years ago = Move legacy apps to Windows Containers - Regan Murphy = 1:02:12
QEtc9A_m3iE = 4 years ago = ASP.NET Core: The One Hour Makeover - Jon Galloway = 59:00
7bfyIsXTddI = 4 years ago = Developing microservices applications on the Kubernetes platform - Shahid Iqbal = 48:48
_FTghtxlUyA = 4 years ago = Porting MVVM Light to .NET Standard: Lessons learned - Laurent Bugnion = 54:17
8JOD1AQGqEg = 4 years ago = The Web That Never Was - Dylan Beattie = 1:01:46
8IXIFuaHAt8 = 4 years ago = Building APIs for developers with Identity Server 4 - Ben Cull = 59:23
L1Ra1qXv79k = 4 years ago = Deploying anything to Azure with Azure DevOps - Damian Brady = 51:50
2-mFWi5oLkM = 4 years ago = The History Of Programming, Part 1 - Mark Rendle = 49:46
ppfLUFO-hwc = 4 years ago = Learn to love meetings - Dr. Neil Roodyn = 1:07:02
YVwISlGCCxw = 4 years ago = WIP: Debugging Depression - Ellen Mey = 48:25
1Hl-BuZY-eE = 4 years ago = What's that fruit? - Scott Holden = 56:30
z_Cb5wQBoXs = 4 years ago = The Visible Developer: Why You Shouldn't Blend In - Heather Downing = 1:01:23
-f5O33T1xxM = 4 years ago = How to avoid UX-traps with a deck of cards - Jessica Engström = 1:02:58
3wbs54XXT2I = 4 years ago = Data lakes beyond clusters - Dom Raniszewski = 1:01:43
i07nBqVXgQc = 4 years ago = What You Need to Know About Open Source—Trust Me, I'm a Lawyer - Jeff Strauss = 1:11:05
UmYv_-vUOLU = 4 years ago = Cross-Platform Desktop Apps with Electron - David Neal = 53:58
nwU5xIOmnKo = 4 years ago = Serverless SQL Pipelines - Lynn Langit = 50:04
DmlzuraxP-c = 4 years ago = Building truly Universal applications with Azure, Xamarin and MVVM - Laurent Bugnion = 1:00:26
yQEgeoabHNo = 4 years ago = Git at Scale - Edward Thomson = 58:09
t4dYy6P3JuA = 4 years ago = Parsing in C# from first principles - Nicholas Blumhardt = 57:35
Wq_p0nfIzZY = 4 years ago = What's new in the Microsoft's Conversational AI Stack - Vishesh Oberoi = 1:00:23
uh4V2IjSrlI = 4 years ago = Kubernetes for .NET Developers - Hossam Barakat = 57:53
jOTmjXS8YFw = 4 years ago = Testing Microservices - Anne-Marie Charrett = 52:21
41mnNyMxPOA = 4 years ago = How We Got Here - The History of Web Development - Richard Campbell = 1:00:47
Kke8BdkvlLc = 4 years ago = Reignite your desire to improve - Richard Banks = 54:36
0h5X5UKWao8 = 4 years ago = Leadership Guide for the Reluctant Leader - David Neal = 50:47
dKqSC0Ii8Bs = 4 years ago = AI on the Edge - Nigel Parker & Dan Glover = 1:01:31
Sf3pu5-xJQA = 4 years ago = Mission Impossible: Lifehack Protocol - Lars Klint = 58:07
04SmFYwLPwM = 4 years ago = What's New In ASP.NET Core - Jon Galloway = 1:00:59
kz7wmRV9xsU = 4 years ago = The Code Behind The Vulnerability - Barry Dorrans = 1:00:37
Nn0JxB9S42w = 4 years ago = Service Meshes - Powering the next wave of microservice architectures - Rob Crowley = 55:45
XfsZ9WnRVXQ = 4 years ago = Flutter from idea to app in 45min - Mitchell Tilbrook = 57:59
dr1i_KPvi08 = 4 years ago = What has 4 years of AWS Microservices taught me? - Abhaya Chauhan = 58:19
HpPGLHKlaM0 = 4 years ago = Lightning Talks - NDC Sydney 2018 - Day 2 = 57:19
14D9VzI152o = 4 years ago = Building Advance Analytics pipelines with Azure Databricks - Lace Lofranco = 48:37
cvo9gCxKj8o = 4 years ago = Broken crypto is broken - Erlend Oftedal = 1:00:47
LZgQBSr36p8 = 4 years ago = Feature Toggles: The Good, The Bad, and The Ugly - Andy Davies = 43:58
_RasVYuv_vA = 4 years ago = Offline UX - Simon Knox = 45:20
I8qw6FmdmdI = 4 years ago = Holo world - Create your first HoloLens app with Unity - Jimmy Engström = 55:12
HUGS2fnu_Y8 = 4 years ago = Attraction and retention strategies for Women in Tech - Donna Edwards = 51:41
TJxXYlO1gxA = 4 years ago = Need for speed 8, performance tuning of your web application - Yaser Adel Mehraban = 57:46
k7U-V4EwoP8 = 4 years ago = Git as Blockchain - Michael Perry = 59:24
4Grmq_9Hq-Y = 4 years ago = How to survive and thrive as an engineering leader - Isabel Nyo = 58:20
TXwCu8fVsVU = 4 years ago = Android TDD with Kotlin - Heather Downing = 50:44
ZwXEild-0t8 = 4 years ago = Moving Fast - without crashing - Marcus Bristol = 1:03:01
DIu1FLD8CsE = 4 years ago = 7 Years of DDD: Tackling Complexity in Large-Scale Marketing Systems - Vladik Khononov = 1:00:06
nKM7CRyhQKg = 4 years ago = Google Home meets .NET containers on Google Cloud - Ankur Kotwal = 1:01:29
a5h2CxQzYaU = 4 years ago = Field Notes : .NET Core and Docker in Production - Damian MacLennan = 54:48
OAz0qfhZneE = 4 years ago = Navigating the React Solar System - Ben Ilegbodu = 1:01:39
Hvp6l42AL8U = 4 years ago = Lessons from a real HoloLens project - Luke Drumm = 58:57
uen8HwFVarc = 4 years ago = Practical design patterns in the age of the cloud - Magnus Mårtensson = 52:02
dYAJLqUfhBs = 4 years ago = Hacking with Go - Victoria Almazova = 1:01:02
av5YNd4X3dY = 4 years ago = Correcting Common Mistakes When Using Async/Await in .NET - Brandon Minnick = 52:12
uFbDh1fYd8Y = 4 years ago = Why I bet my business on React - Jess Telford = 49:11
4vtLZrNRf60 = 4 years ago = How To "Dot" Into Anything, Anywhere, Anytime (Facilitating Data-First Programming)  - Steven Taylor = 55:51
mgPAdKM0UwU = 4 years ago = Cloud Native .NET -Mark Rendle = 1:02:20
1hNs5svtks4 = 4 years ago = NDC London 2019 - Conference for Software Developers = 0:33
YNZoCR695eU = 4 years ago = .NET on Azure - Shayne Boyer = 1:01:50
QvT8Y43HbC0 = 4 years ago = 60 Minutes to Accessibility - Larene Le Gassick = 1:00:09
Mm_RuObpeGo = 4 years ago = Open-Source Maintainers are Jerks! - Nick Randolph & Geoffrey Huntley = 45:25
O-ZcbHmNUHE = 4 years ago = Serverless with Firebase in the wild - Duncan Hunter = 51:03
ndEelfeYLhs = 4 years ago = The Structure of Software Revolutions - Mike Long = 49:44
3Ty08C_yYyk = 4 years ago = The beauty of stupid ideas - Aaron Powell = 51:51
BZg3o8ncPZI = 4 years ago = Power BI for Developers - Peter Meyers = 48:10
cA9nSHz1Njk = 4 years ago = NDC Sydney Lightning Talks = 52:58
65ibyDjxuwM = 4 years ago = Service workers - beyond the cache - Phil Nash = 57:33
GFvFZFFeTD8 = 4 years ago = Serverless Continuous Delivery with the Serverless Framework - Fabien Ruffin = 43:48
5ztMNdCZrRY = 4 years ago = A fistful of Blazor; Its .NET in the browser - William Tulloch = 1:03:36
cQB6EKoRyvU = 4 years ago = ARM FTW – Azure Resource Manager For The Win - Magnus Mårtensson = 47:29
mrXHf71lYrs = 4 years ago = Reading other peoples code - Patricia Aas = 55:44
1t4kYry9jP4 = 4 years ago = Programming for Amazon Alexa - Terence Le Grange & Mahesh Krishnan = 58:37
IwT0YBPzMxo = 4 years ago = Autonomous Exploration Robotics with a Raspberry Pi - Christian Catchpole & Rachael Colley = 1:02:02
J2BdCNpgXQI = 4 years ago = Jewelbots: How to Get More Girls Coding! - Jennifer Wadella = 58:42
dUdGcogYkss = 4 years ago = APIs and Microservices in ASP.NET Core Today and Tomorrow - Glenn Condron = 1:04:45
sG1qfJ_2VSo = 4 years ago = Selling DevOps - Vanessa Love = 50:57
lSGGOL7A-0U = 4 years ago = Deep Learning with TensorFlow - Seth Juarez = 1:05:47
-Ac7z3YEkNI = 4 years ago = The 9 Knights of Azure: Services to Get You Started - Adam Cogan = 1:09:15
lkHNv3_Nw3U = 4 years ago = Mentoring Junior Developers Into Productive Team Members - Daniel Mallott = 1:02:52
FrmQ35pJ7SU = 4 years ago = Creating a ‘best place to work’ culture - Donna Edwards = 53:11
OWdNKrPjbo8 = 4 years ago = Easily Add Artificial Intelligence To Your Apps Using Machine Learning - Brandon Minninck = 54:51
73YcSk2ssbs = 4 years ago = JavaScript Futures—ES2018 and Beyond - Jeff Strauss = 1:00:20
nmWrLqsT-XU = 4 years ago = Introduction to ML.NET - John Alexander = 1:03:42
No6ZQmHukUI = 4 years ago = Deep Learning in the world of little ponies - Galiya Warrier = 1:02:14
EnP3m6aSvwI = 4 years ago = Neural Networks: A Primer - Rishal Hurbans = 57:48
eDYEAzErOiA = 4 years ago = Easier AI allows everyone to build smart apps - Azadeh Khojandi & David Burela = 57:13
3Oc4-cMkGJY = 4 years ago = Getting started with Chaos Engineering - Paul Stack = 51:43
lY6WqQy8LwI = 4 years ago = The conversation every parent dreads - how to talk to your kids about the blockchain - David Burela = 57:25
SUiWfhAhgQw = 4 years ago = Vertical Slice Architecture - Jimmy Bogard = 1:02:01
uxj8Mu0h2G4 = 4 years ago = Empowering the Quantum revolution with Q# - John Azariah = 1:00:34
9V3isdkn1jw = 4 years ago = Designing for speech - Jessica Engström = 59:28
z8DY5DndmxI = 4 years ago = Writing a Neural Net from Scratch - Joe Albahari = 1:03:53
enf3AuWVs48 = 4 years ago = Betting on evolutionary architecture - James Lewis = 58:53
L8c0_QxnT_A = 4 years ago = Sifting Technologies - Separating the Wheat From the Chaff - Nathaniel Schutta = 59:24
F9bznonKc64 = 4 years ago = Get value out of your monad - Mark Seemann = 58:59
hg_5_AUUghY = 4 years ago = What We’ve Learned From Billions of Security Reports - Scott Helme = 56:21
yMB-VSPKDPI = 4 years ago = Security in ASP.NET Core 2.1 - Barry Dorrans = 1:04:21
jdssa77dA5s = 4 years ago = Bots - the next UI revolution - Adam Stephensen = 55:45
PP9DgLUBMUM = 4 years ago = I’m Pwned. You’re Pwned. We’re All Pwned - Troy Hunt = 1:01:31
ukYuhyxXZMc = 4 years ago = Keynote: Apps, Algorithms and Abstractions: Decoding our Digital World - Dylan Beattie = 55:31
LDv7ohdZV1U = 4 years ago = Linux Security APIs and the Chromium Sandbox - Patricia Aas = 46:29
1c4H9ftkHcU = 4 years ago = C++ at High Subsonic Speed - Arne Førlie = 50:00
UWQ4GVVdPYw = 4 years ago = Binary Reproducible Builds with Docker - Mike Long = 42:26
LoJcXmBxIos = 4 years ago = Taking testing to the next level - Ole André Vadla Ravnås = 42:44
OAuRkAAh6Hk = 4 years ago = Everything you want to know about C/C++ pre-processor but couldn't ask - Jon Jagger = 41:26
q6n4Q3lgjSA = 4 years ago = Using Seccomp to Limit the Kernel Attack Surface - Michael Kerrisk = 52:08
JWsiLpb3Sww = 4 years ago = What I Talk About When I Talk About Cross Platform Development - Adi Shavit = 53:12
aOS7N7lRFHU = 4 years ago = What Do We Mean When We Say Nothing At All? - Kate Gregory = 38:56
nOkbSEdClwY = 4 years ago = Designing for consumers, succeeding with professionals - Espen A. Jørgensen = 46:42
LHwxPa0c0D4 = 4 years ago = Zivid One - The story behind the World’s most Accurate, Real time 3D Color Camera - Arild Ulfeng = 44:07
SLjJvvlnYZo = 4 years ago = C++ Cryptozoology - A Compendium of Cryptic Characters - Adi Shavit = 28:48
cAiFJEcqwm4 = 4 years ago = Real-time prototyping using visual programming languages - Rui Martins = 47:10
cQPrtTsM7Zg = 4 years ago = IncludeOS - running C++ applications without an operating system - Per Buer = 45:47
yCNtNKGStv8 = 4 years ago = Sane and Safe C++ Class Types - Peter Sommerlad = 56:31
v77wViQnfus = 4 years ago = Isolating GPU access in its own process - Patricia Aas = 35:15
FTfLLB4kboQ = 4 years ago = C++: No more nulls! (Fixing the billion dollar mistake) - Anders Schau Knatten = 46:23
p4iuZnXzqmI = 4 years ago = Building useful project utils in Python - Johan Herland = 50:33
Fmp9UFjPiJs = 4 years ago = Threat Modeling: uncover vulnerabilities without looking at code - Chris Romeo = 53:20
YvEwQnpMzAc = 4 years ago = Sociocracy for Creating Better Products - Jutta Eckstein = 44:50
vkn4WRVoq_w = 4 years ago = Huddly - The thinking camera and applied machine learning - Mats Gabriel Love Johansen & Kai Wig = 51:09
nCQJHZlxI6g = 4 years ago = Yara Birkeland - a global game changer - An-Margritt Tinlund Ryste = 30:40
HfSWT8zlDvY = 4 years ago = Type safe C++? LOL! - Björn Fahller = 45:46
xm2KyA6NVF0 = 4 years ago = Words of Wisdom - Tony Van Eerd = 45:50
I7z5gvCmKiE = 4 years ago = Self-Awareness in C++ Code - Paul Williams = 42:28
gCQDBz-TMIE = 4 years ago = C++ Unit testing - the good, the bad & the ugly - Dror Helper = 52:33
7KjCOe0oBIw = 4 years ago = The Nightmare of Move Semantics for Trivial C++ Classes - Nicolai Josuttis = 42:23
IGFBCvroXJ8 = 4 years ago = Optimising a small real-world C++ application - Hubert Matthews = 48:10
jm7QsI-nNjk = 4 years ago = The Git Parable - a different approach to understanding Git (90 min) - Johan Herland = 1:25:11
rCk0OcnLMlY = 4 years ago = Agile Development at Scale With Autonomous teams - Thomas Malt & Jan Henrik Gundelsby = 49:04
fkWcxSiI-U8 = 4 years ago = Part II: A Performance Analysis of a Trading System over Compliers - Jason McGuiness = 49:37
uYSl-CvhQTM = 4 years ago = Part I: A Performance Analysis of a Trading System over Compliers - Jason McGuiness = 48:01
DFQT1YxvpDo = 4 years ago = Fuzzing with AFL - Erlend Oftedal = 45:02
fod0IRN3TDk = 4 years ago = SW Testing: Can ML save us? - Marius Liaaen & Carl Martin Rosenberg = 46:08
QtuvfNDC6cw = 4 years ago = How to Transform Developers into Security People - Chris Romeo = 52:20
zHJHwAP7Owg = 4 years ago = Microservice Architectures in Embedded Linux and FreeRTOS - Tore Martin Hagen = 32:55
4kjofLTXenA = 4 years ago = An introduction to Behaviour Driven Development (BDD) for embedded systems - Seb Rose = 49:33
MwmKC8jab0w = 4 years ago = Great UX, Despite Agile: How to Get the Best Out of Your Design Team in Agile Projects - Aras Bilgen = 45:04
YigfTD8YZHw = 4 years ago = "Who do I innovate for?" A Product Manager's perspective! - Shubham Bhattacharya = 38:01
auSGvmVjdDQ = 4 years ago = The Golden Age of Design - Paal Holter = 38:07
tHepctS09uQ = 4 years ago = CUDA Kernels with C++ - Michael Gopshtein = 36:29
YReJ3pSnNDo = 4 years ago = Integrate Python and C++ with pybind11 - Robert Smallshire = 48:20
qanlh_-MmQ8 = 4 years ago = Reflections around SW obsolescence - Andreas Bredesen = 43:51
QC2jQI7GLus = 4 years ago = Unlocking secrets of proprietary software using Frida - Ole André Vadla Ravnås = 51:33
PtjBblkS-Zk = 4 years ago = A Modern Embedded Product Platform - Anders Norman = 42:42
kWBoCXGAOmw = 4 years ago = Working with C++ Legacy Code - Dror Helper = 45:26
oFt6V56BOlo = 4 years ago = Strace: Monitoring The Kernel-User-Space Conversation - Michael Kerrisk = 45:21
jsVZFmx3XIg = 4 years ago = User Research For Everyone - Aras Bilgen = 35:41
WTKODa3UCa4 = 4 years ago = Design for Test - Hubert Matthews = 49:29
Rbl3h0RJuuY = 4 years ago = Higher order functions for ordinary C++ developers - Björn Fahller = 43:21
RWCadBJ6wTk = 4 years ago = Introduction to Lock-free Programming - Tony van Eerd = 52:31
uNq3QFKXdKA = 4 years ago = C++ (Core) Guidelines - Safer C++ - Peter Sommerlad = 48:48
Ic2y6w8lMPA = 4 years ago = Simplicity: Not Just for Beginners - Kate Gregory = 50:56
26RzXVGBnHE = 4 years ago = C++17 in Practice - The good and the ugly - Nicolai Josuttis = 58:02
VoHOLDdfDhk = 4 years ago = Keynote: What can C++ do for embedded systems developers? - Bjarne Stroustrup = 1:08:15
eXzK1WkFjRU = 4 years ago = Low power cellular for the IoT - Peder Rand = 55:22
IROSd7uB-tg = 4 years ago = Writing simpler ASP.NET Core - Jonathan Channon = 55:38
B2JaopmI8-s = 4 years ago = Getting Started with your First Mining Rig! - Clarence Chng & Wei-Meng Lee = 54:09
5WY5QOabykE = 4 years ago = Turn specs into high quality apps - Marco Kuiper = 55:25
hKdNXWg1xao = 4 years ago = Getting benefits of OWASP ASVS at initial phases - Oleksandr Kazymyrov = 35:05
lo7zm0_7x_w = 4 years ago = Breaking Your Code in New and Exciting Ways - Michael Newton = 1:01:08
_jGv4q5-HTQ = 4 years ago = The Digital Transformation is not Digital - Eline Giskeødegård = 1:03:17
7T0WskfVgp4 = 4 years ago = JavaScript the Cute Parts - Venkat Subramaniam = 1:01:58
XtaqRVCn1ZU = 4 years ago = When your Twin is Digital. And in 3D - Petri Wilhelmsen = 55:33
s7KF81l57Zc = 4 years ago = Super large, ultra fast, mega scaling cloud computing - Espen Brandt-Kjelsen = 50:43
NymRSKQ12h4 = 4 years ago = Gotchas using Terraform in a secure delivery pipeline - Anton Babenko = 1:00:28
vRqcUS4CPFs = 4 years ago = Attacking Modern Web Technologies - Frans Rosén = 54:58
kvTostlJp7M = 4 years ago = Dos and Don'ts for Serverless and Azure Functions - Jeff Hollan = 1:01:22
1_7e4AyiYd8 = 4 years ago = Stop reinventing the wheel with Istio - Mete Atamel = 52:39
_-rxEBK97CQ = 4 years ago = Kubernetes for .NET developers - Shahid Iqbal = 49:38
iMM4Nq9Xqw0 = 4 years ago = The History of .NET - Richard Campbell = 51:35
EGHtWgNAIbg = 4 years ago = Google Home meets .NET containers on Google Cloud - Ian Talarico & Mete Atamel = 1:00:45
RBnPvQQ36mA = 4 years ago = Docker, FROM scratch - Aaron Powell = 59:59
Z4eICqcsFi0 = 4 years ago = Managing your Black Friday Logs - David Pilato = 1:00:53
YP5vjNnkOkY = 4 years ago = Overcoming a million reasons not to be HTTPS only - Halvor Sakshaug = 48:06
M49NGlmrbGA = 4 years ago = Deploy microservices confidently using Consumer Driven Contracts - Henrik Stene = 10:19
X8UtWzbMVac = 4 years ago = Integrating visual testing into the build pipeline - Shokoofeh Hesari = 12:23
_3eaVy8c-xk = 4 years ago = Machine learning algorithms, choosing the correct algorithm for your problem - Joakim Lehn = 9:13
3qLrMEq7ep0 = 4 years ago = Dr AI, cure my low back pain! - Tale Prestmo = 9:38
SEM8r3u2wEk = 4 years ago = The History of AI - what can we learn from the past? - Håkan Silfvernagel = 12:02
UyK9geJasjE = 4 years ago = Type-safety in low-level programming: Modern C++ in game console emulators - Tony Wasserka = 1:04:10
26pWkYXiw9g = 4 years ago = Rapid App Development With React Native: Lessons Learned at NSB - Eirik Wendel = 1:00:51
1LXgrm7brGA = 4 years ago = Keyboards? Where we’re going, we don’t need keyboards. - Don Wibier = 53:40
6sWa4aAOjQo = 4 years ago = How FINN.no went from being search engine hostile to be a little bit friendly - Henning Spjelkavik = 37:33
BM_WCEB985U = 4 years ago = Let’s Talk About Mental Health - Arthur Doler = 1:03:31
aZGf522Ykcg = 4 years ago = Constructing Modern UIs with SVG - Tim G. Thomas = 53:12
KWJ30qZvtsY = 4 years ago = Behind the AI Curtain - Designing for Trust in Machine Learning Products - Crystal C. Yan = 33:07
KGIGFHVoZo0 = 4 years ago = 12 Factor MicroServices - Andy Davies = 53:52
GaEKjibCEtI = 4 years ago = Not a magic : What to expect from Machine Learning projects - Katya Mustafina, Natalia An = 51:04
WPBNVasv6MQ = 4 years ago = Information saves lives - Anine Kongelf & Einar Ingebrigsten = 1:05:38
uYU-3wv4a9o = 4 years ago = Kotlin for the curious - Matt Ellis = 53:17
nH8YZvfLa4M = 4 years ago = The Future of Data Visualization on the Web - Alan Mendelevich = 42:41
u7sH6Y74GZA = 4 years ago = Security Holes in Git - Edward Thomson = 54:26
dWmKAMSKlfU = 4 years ago = Deep Learning with CNTK and F# - Mathias Brandewinder = 57:15
w8Dv1TEguJ8 = 4 years ago = Implementing Event-Driven Microservices architecture in Functional language - Nikhil Barthwal = 58:55
cR63bGHT0F4 = 4 years ago = Simple Guide to Secure SDLC - Audrey Nahrvar = 25:57
DIDuuxezokU = 4 years ago = NDC TechTown 2018 - Software development for products = 0:29
ycUiRvJdreM = 4 years ago = F# and Fable: re-think web development - Maxime Mangel = 55:23
RRcnFd9TbjI = 4 years ago = Refactoring to Functional Style - Venkat Subramaniam = 55:22
j9C3PJK4S9g = 4 years ago = Become a Wireless Connectivity Ninja 101 - Joakim Lindh = 53:17
2fVItYQ5YSQ = 4 years ago = IoT is fun using MicroPython - Sebastian Roll = 1:04:58
4x2qLgz9SqU = 4 years ago = Prison Break - When the web escapes the browser - Dominik Kundel = 54:44
iLXktgplt4o = 4 years ago = The Hello World Show = 56:39
mRuaMet6aWo = 4 years ago = **Freaking computers, how do they work? - Code Inception** - Michal Luziak = 44:49
84zwBevkqLA = 4 years ago = Everything is awesome: the Lego approach to being an awesome coworker - Paul Verbeek-Mast = 57:08
mZoTjyH1BAI = 4 years ago = Accessibility vs latest Web APIs. Can’t we just get along? - Mauricio Palma = 45:51
Br1024ULnkM = 4 years ago = What and where? - Machine learning for geospatial image analysis - Mathilde Ørstavik = 33:08
02gpZuK5gF8 = 4 years ago = Deconstructing Privilege - Patricia Aas = 48:53
mZNaDyMXW_M = 4 years ago = I just hacked your app! - Marcos Placona = 45:08
0fpDlAEQio4 = 4 years ago = Four Languages from Forty Years Ago - Scott Wlaschin = 1:01:45
XUm0bzpvTzQ = 4 years ago = Blockchain, Smart Contracts, and Ethereum - Wei-Meng Lee = 1:04:14
XWTrcBqXi6s = 4 years ago = Building Event-Driven Microservices with Event Sourcing and CQRS - Lidan Hifi = 44:44
x7dJD3KTxb4 = 4 years ago = How to be a better interviewer - Suzi Edwards Alexander = 1:03:34
SuZZV74wTkw = 4 years ago = What Doctors Can Teach Us on Continuous Learning - Johnny Graber = 53:43
XQ4qYvKX4Uw = 4 years ago = The Enterprise DevOps Challenge - Roy Osherove = 1:02:20
_sZT0CpJ6Vo = 4 years ago = Immutable application deployments with F# Make - Nikolai Norman Andersen = 54:04
eM4xb9aemDU = 4 years ago = Containers in Production: It’s Like Orchestrating Cats - David Ostrovsky = 1:02:29
wDY_SPfed7c = 4 years ago = The Pyschology of Social Engineering - Niall Merrigan = 52:52
1Rna6NvIIDk = 4 years ago = People that make computers go crazy - Gojko Adzic = 1:00:36
8yBPDr_I9Zc = 4 years ago = Neural Networks: Where do I start?!? - Chase Aucoin = 39:55
VD4cDcyQI2o = 4 years ago = Notorious B.I.G. Data: Wins and fails when building a big data platform in the cloud - Andreas Heim = 26:59
spGwfQIy1sM = 4 years ago = When will we have a Rosie of our own? - Amber McKenzie = 45:40
lepKIVH3ZfE = 4 years ago = TypeScript Decorators - Higher Order Functions in Disguise - Damjan Vujnovic = 46:29
F8UUrjTtalE = 4 years ago = Betting on Evolutionary Architecture - James Lewis = 52:26
tVnIUZbsxWI = 4 years ago = Finding your service boundaries - a practical guide - Adam Ralph = 57:54
64X8rCy1jSA = 4 years ago = Dates and times aren't that hard - honestly! - Jon Skeet = 1:00:02
C1mdqVD3HMo = 4 years ago = Serverless with Firebase in the wild - Duncan Hunter = 50:53
X03WqRoNZek = 4 years ago = Hacking your work life __ balance to take over the world - Jennifer Wadella = 59:10
-50ntzz18XU = 4 years ago = Implementing Authentication and Authorization with ASP.NET Core 2 - Chris Klug = 1:03:45
9ZRZQq4tYLw = 4 years ago = Serverless architectural patterns - Yan Cui = 50:37
QsZWye0G9hI = 4 years ago = Pilot Decision Management - Clifford Agius = 1:00:57
MyP1VFHdxKY = 4 years ago = Actors in clusters: why, when and how - Pawel Banka, Vagif Abilov = 59:10
zXtTFXziEmQ = 4 years ago = Security in Cloud-Native - Robin Minto = 51:44
DEeOFE_DreU = 4 years ago = Hacking 4G and how to get arrested in 10 minutes - Christian Sørseth = 8:25
MhSOAk69JlM = 4 years ago = ACME TLS-SNI-01 issuing Let's Encrypt SSL-certs for any domain using shared hosting - Frans Rosén = 11:07
cqZ-nQr-Q2M = 4 years ago = C++ Cryptozoology - A Compendium of Cryptic Characters - Adi Shavit = 16:37
Uy7SYbwYBT8 = 4 years ago = Lightning Talks: Secure Communication between Extensions and Applications - Pavel Studený = 8:16
x6F97CAUki0 = 4 years ago = Lightning Talks: Breaking into Security - Audrey Nahrvar = 16:11
vlkeleMJIpo = 4 years ago = Securing the last mile of IoT solutions - Anders Lybecker = 57:19
yQXQskiiDNU = 4 years ago = Type safe C++? LOL! - Björn Fahller = 49:47
gHGMDFm2MVs = 4 years ago = Secure Programming Practices in C++ - Patricia Aas = 50:45
u-IVTi0W0ro = 4 years ago = Mötley Crüe and Mödern JavaScript - Eric Brandes = 50:01
pGCHAJnJ1CA = 4 years ago = Adapting ASP.NET Core MVC to your needs - Filip W = 1:00:46
dPTx5s2VWMg = 4 years ago = "Hello, Multiverse!" - Quantum Computing and You - John Azariah = 54:37
6OJvR-L43ys = 4 years ago = Architecting your next SPA - Guy Nesher = 56:20
SgnE3p1qF-c = 4 years ago = 2018 - The Year of Web Components - Dominik Kundel = 58:49
di_eKZ39tN8 = 4 years ago = Five ways to be a happier JavaScript developer - Christian Heilmann = 33:02
Ygk9CCRWOJs = 4 years ago = How to teach programming and other things? - Felienne = 43:13
qiX2rujq1aQ = 4 years ago = Ditching Promises and Socially Acceptable Callback Hell - Brandon Satrom = 33:30
fRgFVNhSJEc = 4 years ago = NDC 2018   Dag 2   Sesjon 5   Sal 4Deconstructing TypeScript’s Type System - Spencer Schneidenbach = 1:00:34
nQvysf00cHA = 4 years ago = Event Driven UIs - Matt Barrett, Bhavesh Desai = 46:51
UB6iROIB0d8 = 4 years ago = Using Kafka for Real-Time Data Ingestion with .NET - Kevin Feasel = 57:12
VTosiG6656A = 4 years ago = "Beyond the Usual Suspects, Emerging Cognitive Services" - Hank Boelman = 46:43
RwFFBW7zVTc = 4 years ago = From SQL to Azure Cosmos DB - Jimmy Bogard = 1:02:23
7AJR66p5E4s = 4 years ago = The Erlang Ecosystem - Robert Virding = 1:01:26
TRLYjp0c_as = 4 years ago = From Reactive Extensions to Reactive Streams - Bartosz Sypytkowski = 1:01:29
tT2E3dyFZLU = 4 years ago = Modern Security with Microservices and the Cloud - Sandeep Dinesh = 41:15
yL7xBhWrdKw = 4 years ago = The F# Path To Relaxation - Don Syme = 1:01:19
qBYVW4ghMi8 = 4 years ago = Dependency Injection revisited - Mark Seemann = 56:02
5uKR3Py6ejo = 4 years ago = The Curious Case of Freya, Suave and Giraffe: reducing risks in picking a new tech - Gien Vershatse = 51:26
TD9GZ5HSEmA = 4 years ago = Billions of Sensors - The UX Beyond the Screen - Niklas Norin = 55:39
xC0yn8r3PTQ = 4 years ago = Enough string_view to hang ourselves - Victor Ciura = 59:47
7uAwFRQkzyA = 4 years ago = C++: Be type-safe - The journey of determining the number of elements in an array - Andreas Fertig = 53:06
a19juaN01E8 = 4 years ago = Reverse Engineering a Bluetooth Lightbulb - Jesse Phelps = 49:17
L-z4kdgccas = 4 years ago = Despagghetifying code with NDepend - Jim Pelletier = 57:40
xw6uyxJ3SKY = 4 years ago = ♫ These are a few of my favourite (Android) Things ♫ - Marcos Placona = 52:00
yayptECOtr8 = 4 years ago = Web Application Security Trends - Christian Wentz = 58:55
T1k_IyI50ag = 4 years ago = Google Assistant VS Alexa: Battle of the Bots - Heather Downing = 52:12
BrGQ738KdgM = 4 years ago = How to network if you’re scared of people - Kasia Rachuta = 29:28
_YfNdwGswRA = 4 years ago = Choose your own adventure: the tech career version - Nabeelah Ali = 37:23
m_e36bBQxrk = 4 years ago = Domain-Driven Design: Hidden Lessons from the Big Blue Book - Nick Tune = 38:47
f0E8AFpVvVc = 4 years ago = Muddling Through The Middle Bits: what comes after Junior and before Senior - Anne Cahalan = 35:36
W0Lui4HlHkk = 4 years ago = Rise of the Tech Influencer - Small steps you can take to increase your reach - Michelle Sandford = 52:41
qDB3q1FvpXQ = 4 years ago = Productivity Bots - Marcus Bristol = 1:01:48
c9mhpFSDR7I = 4 years ago = Drone CI vs Jenkins. Fight!- Niklas Hole, Ole Anders Stokker = 39:13
KhkcBIjul3o = 4 years ago = Taming Infrastructure Workflow at Scale - Anubhav Mishra = 1:01:07
AgXOEhBqdYc = 4 years ago = Monitoring A-Z - Steve Simpson = 58:47
z26tFw2OMJY = 4 years ago = Manifesto for a DevOps-like Culture Shift in Data & Analytics - Sean Gustafson, Arif Wider = 58:19
JL4lXFtyFr0 = 4 years ago = The 9 Knights of Azure: Services to Get You Started - Adam Cogan = 1:10:06
9Zu4JoH2s9A = 4 years ago = Building and Training your own Custom Image Recognition AI - David Giard = 1:03:36
LOOXRDNugRM = 4 years ago = A Practical Guide to Graph Databases - David Bechberger = 55:14
-rGo-wsQeWM = 4 years ago = Understanding Alexa - Jeff Blankenburg = 1:04:32
h43uM2dOKl0 = 4 years ago = What We’ve Learned From Billions of Security Reports - Scott Helme = 50:59
Hi-P-yOAT-s = 4 years ago = Deep Learning with TensorFlow - Seth Juarez = 1:06:39
IXV4XqX8UVc = 4 years ago = I’m Pwned. You’re Pwned. We’re All Pwned - Troy Hunt = 1:01:35
CXyNZYDO07Q = 4 years ago = Technical debt isn't technical - Einar W. Høst = 38:39
iIhUOX_TJuA = 4 years ago = The State of C# - What Have I Missed - Filip Ekberg = 55:13
5CQNevxzEew = 4 years ago = Give it a REST - Tips for designing and consuming public API's - Liam Westley = 54:32
TYb-vw6knQ0 = 4 years ago = Containers and Serverless with AWS - Norm Johanson = 52:30
IAcxetnsiCQ = 4 years ago = Implementing the Clean Architecture in .NET Core - Ian Cooper = 1:01:34
0ziPM11gc2g = 4 years ago = Insecure Transit - Microservice Security - Sam Newman = 1:01:54
OexK0f4dOlQ = 4 years ago = The IoT Requires Upgradable Security - Lars Lydersen = 34:50
1YqnaUXcSl8 = 4 years ago = ClojureScript - It's not just the language - Christian Johansen = 50:03
gDO1YdNBkl4 = 4 years ago = Succeeding with Xamarin - Filip Ekberg = 54:29
fZWx8whOz10 = 4 years ago = Lightning Talks: Tell me the money! How I made my bank talk to me by way of PSD2 - Anders Breivik = 11:00
IUBi3wupRp8 = 4 years ago = Lightning Talks: PWA - A Farewell To Apps - Andreas Ahlgren = 12:32
hUBYxZIB-FU = 4 years ago = A Failed Project and the Technical Architecture That Saved It - Dominic Robinson = 11:08
Iv3px26XKl8 = 4 years ago = Lightning Talks - The Power of Inclusion - Dennie Declercq = 16:32
88K8oO_dYbI = 4 years ago = Frontend Development 2018 - What's in your stack? - Stefan Judis = 49:55
2ADqzROC05I = 4 years ago = Lightning Talks - What's in a name? - Meg Gotshall = 10:05
kcBlSmo3Xlk = 4 years ago = Higher order functions for ordinary C++ developers - Björn Fahller = 1:02:53
qxb62AErRWw = 4 years ago = An Opinionated Approach to ASP.NET Core - Scott Allen = 55:38
WIgUmnwKdas = 4 years ago = Protecting Encryption Keys with Azure Key Vault - Stephen Haunts = 58:45
7f9CuTlbNLQ = 4 years ago = How I Learned to Stop Worrying and Love the Website - Jackie Balzer = 43:27
t34Cff0pBmA = 4 years ago = Authorization for modern Applications - Dominick Baier = 54:01
gGUYUJmssYM = 4 years ago = C# 8 - Jon Skeet and Mads Torgersen = 1:00:54
wgoPa5Kn0n0 = 4 years ago = Database as API with PostgreSQL and Massive.js - Dian Fay = 49:24
eUo3oiY1-98 = 4 years ago = Building an Azure IoT pipeline for LoRaWAN devices (live demo) - Ronnie Sauremann = 1:01:51
jK8jYQ3ZKiI = 4 years ago = So you want to create your own .NET runtime? - Chris Bacon = 1:02:28
nXljhGDokqA = 4 years ago = The Power of Roslyn - Kasey Uhlenhuth = 1:00:47
_qyxGGpVj_E = 4 years ago = Lightweight microservice collaboration using HTTP - Christian Horsdal = 52:12
9CSjlZeqKOc = 4 years ago = The Web That Never Was - Dylan Beattie = 59:39
Bnm71YEt_lI = 4 years ago = Build your own Excel 365 in an hour with F# - Tomas Petricek = 1:00:55
deHj2lG5qOY = 4 years ago = Reinventing MVC pattern for web programming with F# - Krzysztof Cieślak = 59:43
Mu39vtwKWpg = 4 years ago = Why you should use F# - Phillip Carter = 57:56
6rjhrc4SEqM = 4 years ago = A Practical Introduction to Data Science - Mark West = 45:15
qrjHYXFy62E = 4 years ago = Tabs, spaces and salaries: a data science detective story - Evelina Gabasova = 46:18
WhEkBCWpDas = 4 years ago = The Power of Composition - Scott Wlaschin = 1:01:32
YgGirHah_aU = 4 years ago = Cellular Connectivity for IoT - Albert Skog = 48:21
FXgVpFZ0duQ = 4 years ago = Agile Software Architecture - Ian Cooper = 1:03:28
t5gVCirCw1I = 4 years ago = What I Talk About When I Talk About Cross Platform Development - Adi Shavit = 1:02:37
6RlloT_6WxA = 4 years ago = Fastware - Andrei Alexandrescu = 1:01:32
rWZXjz_nnzs = 4 years ago = Internals of Exceptions - Adam Furmanek = 50:01
nVzgkepAg5Y = 5 years ago = Expect the Expected - Andrei Alexandrescu = 1:01:02
J_QLQPJlHro = 5 years ago = A developers guide to Machine Learning - Tess Ferrandez-Norlander = 59:14
4IsAaFa195I = 5 years ago = A Penny for Every Object - Mads Torgersen = 1:09:55
HoDRRe4tNng = 5 years ago = User Experience for Professionals - Paul Holter = 58:55
7vPh-xy-kyc = 5 years ago = Beautiful code: typography and visual programming - Peter Hilton = 48:51
67a4Vm-6_Xo = 5 years ago = Automatically categorizing news articles on nrk.no - Øyvind Holmstad = 38:08
peT6NbKfwzw = 5 years ago = Jewelbots: How to Get More Girls Coding! - Jennifer Wadella = 56:46
Jrjd5lfkzMk = 5 years ago = We Didn’t Stop to Ask If We Should: Understanding Build vs. Buy - Todd Gardner = 35:12
THRXtRHNT6E = 5 years ago = Blockchain, Smart Contracts, and Ethereum - Wei-Meng Lee = 1:01:12
j51Fmn4JVwU = 5 years ago = The Web That Never Was - Dylan Beattie = 55:02
W5JcMQdMexs = 5 years ago = Introduction to webpack - Chris Klug = 1:02:45
GtTiIY51kK0 = 5 years ago = Contract First API Design with OpenAPI V3 - Darrel Miller = 1:00:10
A5VTdACQtIM = 5 years ago = How to Build a Smart Garage Door Opener / Sensor for Under $100 - Matt Milner = 57:53
EXebOr6gNZc = 5 years ago = Designing for Trust - Crystal C. Yan = 42:55
t_z0snOulB0 = 5 years ago = TECHRADAR #3 = 1:52
E7ex48m1R9w = 5 years ago = NDC Oslo - TechRadar #2 = 1:35
g00SazhwAwQ = 5 years ago = NDC Oslo - TechRadar = 1:27
Yic-Gx10e6o = 5 years ago = Practical Ghostbusting: Meltdown, Spectre and You - Ian Coldwater = 50:07
RzYZkIN_cqM = 5 years ago = Running containerized applications on Azure Container Services - Marcel de Vries = 1:09:18
BSYbVNmf41U = 5 years ago = It’s Dangerous To Go Alone! Take This Team. - Trent Willis = 52:20
OV94p_kB-Lg = 5 years ago = What You Need to Know About Open Source—Trust Me, I’m a Lawyer / Jeff Strauss = 1:04:29
IURCU4GcnB8 = 5 years ago = “Hello, Multiverse!” - Quantum Computing and You - Simon Middlemiss = 54:19
MbCjh953wA0 = 5 years ago = Browser Invasion: Desktop Apps and the Web - Tim G. Thomas = 55:35
WjQVJssSpt8 = 5 years ago = Modern TypeScript is amazing! - Jake Ginnivan = 49:26
wBVFJv_urXA = 5 years ago = Setting Fire To My Desk: Adventures in Redis and Microcontrollers - Kyle Davis = 48:29
uOm0LzajkNM = 5 years ago = Let’s Make A Website, Right Frickin’ Now! - Lemon = 45:23
3ZbYCtnwPsY = 5 years ago = Building Scalable, Maintainable Apps Using TypeScript and React - Kamran Ayub = 56:37
KBdFgJuzFck = 5 years ago = Home Alone: How working for a fully remote company actually works - David Boike = 45:58
77Dk3vjVa9k = 5 years ago = Cloud Native .NET - Mark Rendle = 1:02:58
5H_yWNAMH-Y = 5 years ago = Introduction to Natural Language Processing with Python - Barbara Fusinska = 47:41
Ff0dac7CFv4 = 5 years ago = The Death of Data: Risk, Retention, and Rot - Heidi Waterhouse = 43:11
TqT7u1Tjp2M = 5 years ago = Who Needs Dashboards? - Jessica White = 34:43
II9FuVkMBXQ = 5 years ago = From SQL to Azure Cosmos DB - Jimmy Bogard = 1:01:27
itHPmcOQY8Q = 5 years ago = Analyzing StackExchange with Azure Data Lake - Tom Kerkhove = 1:02:13
XjMTDb20O7M = 5 years ago = Why you should never build Microservices - and why we do it anyway - Martin Larsen = 1:07:40
EsVaEVWSvwI = 5 years ago = Surviving Microservices - Michele Bustamante = 57:11
iDnLNlK4KXw = 5 years ago = The Hello World Show LIVE at NDC Minnesota 2018 = 1:06:57
WLm01e7jPLo = 5 years ago = Docker Containers on Azure - let me count the ways - Michele Bustamante = 1:07:28
1RetLodCL1g = 5 years ago = Containers without Docker - Ben Hall = 48:54
x02IXM0QYAc = 5 years ago = Docker On Windows 101 - Ashley Poole = 46:56
W5aCLRgxTvk = 5 years ago = Implementing authorization in web applications and APIs - Brock Allen = 57:39
sgXq5-UGRt8 = 5 years ago = Serverless Applications with AWS - Norm Johanson = 54:13
4XNjuzUXj8o = 5 years ago = The whirlwind tour of Authentication and Authorization with ASP.NET Core - Chris Klug = 59:25
-8Kj58XYoTg = 5 years ago = Your Car “Knows” You: Security in Connected Vehicles & Roadway Infrastructure - Tiffany Rad = 1:04:27
BIgIw7k9a0k = 5 years ago = Bigger, Faster and More Secure - Laura Bell = 50:38
JlffiyxiPPQ = 5 years ago = Protecting Encryption Keys with Azure Key Vault - Stephen Haunts = 57:24
0EWiSJj0q_0 = 5 years ago = Leadership Guide for the Reluctant Leader - David Neal = 49:49
tFgKs4r4LM0 = 5 years ago = Cross-Platform Desktop Apps with Electron - David Neal = 57:47
d0lxRcoqMqk = 5 years ago = Cloud, Containers, Kubernetes - Bridget Kromhout = 1:01:04
uKqs7cLWSO4 = 5 years ago = Angular Unit Testing from the Trenches - Justin James = 56:15
LzgJaAMjmoE = 5 years ago = Push it (Push it Real Good) - Lyndsey Padget = 1:07:13
SJONJOHyrq4 = 5 years ago = Ionic, ngrx and Angular: building web and mobile apps with one code base - Duncan Hunter = 1:13:26
MIaHx3AX-Zw = 5 years ago = Up and Running with Progressive Web Apps - Nik Molnar = 1:01:49
x6vn572JP0o = 5 years ago = Creating airplane mode proof Xamarin applications - Gerald Versluis = 1:04:05
hAdhirDmjCQ = 5 years ago = Go Mobile with Xamarin - Brent Edwards = 1:00:30
U_-wCQWXgbM = 5 years ago = Lightning Talks - Fear of the Bus: Docs and DevOps - Heidi Waterhouse = 20:42
hyHBIxeGg5M = 5 years ago = Lightning Talks - Leveraging APIs to Transform Healthcare - Crystal C. Yan = 12:31
kfkipOA2iHE = 5 years ago = Lightning Talks - Angular2+ Reactive Forms - Lyndsey Padget = 18:55
D1JDGHlnWnc = 5 years ago = Introduction to Python - Austin Bingham = 1:00:26
24fQBEMBTnc = 5 years ago = Augmented Reality: The Lion, The Witch and The Robot - Lars Klint = 51:42
dS57qP_kzU4 = 5 years ago = Machine Learning for Gamers - Dungeon Forecasts & Dragon Regressions - Guy Royse = 46:39
4hvIwRHylj0 = 5 years ago = Dependency Injection revisited - Mark Seemann = 54:15
wN4w07polhk = 5 years ago = Intelligent Interfaces with Cognitive APIs, BOTs and IOT - Ian Philpot & Anu Prasad = 59:45
hMRrqkl77rI = 5 years ago = Deep Learning with CNTK and F# - Mathias Brandewinder = 57:27
CCX8Sox6BNQ = 5 years ago = Own the future, NSB-style - Udi Dahan = 1:13:22
2iYdKQXGY2E = 5 years ago = Own the future - Udi Dahan = 55:44
WMdBoeQtxUY = 5 years ago = An Opinionated Approach to ASP.NET Core - Scott Allen = 56:33
JU-6pAxqAa4 = 5 years ago = Blazor, a new framework for browser-based .NET apps - Steve Sanderson = 1:02:58
TPS-eFmdepw = 5 years ago = Keynote: Apps, Algorithms and Abstractions: Decoding our Digital World - Dylan Beattie = 58:08
FTBk62s3OGY = 5 years ago = NDC Minnesota - 7-10 May 2018 = 1:35
glBUgD-qVYI = 5 years ago = NDC Security Australia - 14-16 May - Gold Coast = 0:46
kDFvYqCNkvQ = 5 years ago = NDC Minnesota 2018 = 1:10
S-V3hgrJCxo = 5 years ago = NDC Mini Copenhagen 2018 = 2:15
iAGDVAiTCvA = 5 years ago = Serverless - the brief past, the bewildering present, and the beautiful (?) future - Mike Roberts = 58:29
0b3PiOoHUp0 = 5 years ago = How to parse a file - Matt Ellis = 58:44
2176f9K-cC4 = 5 years ago = Anchor Modelling: Sixth Normal Form Databases! - Stephanie Locke = 1:06:37
66fcoX7kt7Y = 5 years ago = The Hello World Show Live with Scott Hanselman, Troy Hunt, Felienne, and Jon Skeet = 57:48
9G8HEDI3K6s = 5 years ago = Web Apps can’t really do *that*, can they? - Steve Sanderson = 1:00:40
B_CtanauwxY = 5 years ago = Running .NET Containers on Google Cloud - Chris Bacon & Mete Atamel = 1:00:14
DfhmOScEVPQ = 5 years ago = What C# Programmers Need to Know About Pattern Matching - Eric Potter = 52:57
GJ6Ogin5W0s = 5 years ago = GitOps - Using Git as your source of truth for build, deploy and observability - Alexis Richardson = 47:13
JxwRrQJoRas = 5 years ago = Mobile Architecture at Scale - Gergley Orosz = 1:00:19
KfM-3pkWznw = 5 years ago = The Modern Cloud - Scott Guthrie = 1:02:23
MxnGYtFVEzM = 5 years ago = Easier AI allows everyone to build smart apps - David Burela & Azadeh Khojandi = 1:02:44
QNA9EExd8lQ = 5 years ago = Pilot Decision Management - Clifford Agius = 58:37
S30QXoqLyig = 5 years ago = Painless visual testing - Gojko Adzic = 53:19
Z2dE7OpL0Fc = 5 years ago = Nginx for .NET Developers - Ian Cooper = 1:03:15
aAsVbUyypfs = 5 years ago = Testing in Production - Gel Goldsby = 1:03:08
aKkzIoQfIvs = 5 years ago = Developing for Mixed Reality with HoloLens - Rafał Legiędź = 1:07:40
b4YKD-Rm8ow = 5 years ago = Inclusive Design Series: How to stop worrying and love accessible forms - Elle Waters = 1:06:36
jF36MiP2GYw = 5 years ago = Jewelbots: How to Get More Girls Coding! - Jennifer Wadella = 52:46
kpbeaMOTOxM = 5 years ago = Succeeding with Xamarin - Filip Ekberg = 58:07
lp_NhaxqFG8 = 5 years ago = Xcode to Unreal Engine - Lessons Learned from Doing the Impossible - Ellen Mey = 48:43
pDgWX1N1mgI = 5 years ago = Tips & Tricks with Azure - Scott Guthrie = 1:08:42
rTPbKzvDHDI = 5 years ago = The Psychology of Social Engineering - Niall Merrigan = 53:17
uHzGwQfJIWo = 5 years ago = Why you should use React Native for your next mobile app - Gwendolyn Faraday = 51:38
zBW8Lj6XcHc = 5 years ago = How to win with automation and influence people - Gwen Diagram = 52:19
2Vo-aMOyqbw = 5 years ago = The data dichotomy: Rethinking data and services with streams - Ben Stopford = 55:20
8brpq7DdFIs = 5 years ago = Building real-time API's with GraphQL - Sandeep Singh = 1:04:26
ACHr-qwHS8Y = 5 years ago = Observability: it's not just an ops thing - Charity Majors = 51:34
dToSgOkTZBI = 5 years ago = Styleguide-Driven Development - Arvid Torset & Tatiana Kolesnikova = 1:05:22
7z-WZi2Nb-Y = 5 years ago = Designing for speech - Jessica Engström = 54:52
CmS6ta17VLk = 5 years ago = What is .NET Standard? - Adam Ralph = 1:01:09
P1xdpY7FEMc = 5 years ago = Speak To Me: Voice App Conversation Practices - Heather Downing = 50:05
UrfqA7ShYE0 = 5 years ago = Sonic Pi - Sam Aaron = 58:41
h7hEVJaI3Nw = 5 years ago = Amazon Machine Learning to Predict Responses - Kesha Williams = 1:05:32
hjpUHZY5-18 = 5 years ago = A developers guide to Machine Learning - Tess Ferrandez-Norlander = 1:01:41
tIOZasGMrP8 = 5 years ago = Networks are like onions: Practical Deep Learning with TensorFlow - Barbara Fusinska = 1:01:31
LgAtQF_XvTw = 5 years ago = The Performance Investigator's Field Guide - Sasha Goldshtein = 1:00:50
PuDE99ue8SU = 5 years ago = What is this cloud native thing anyway? - Sam Newman = 57:18
c8ppFCPLgMU = 5 years ago = Deploying Windows Container based apps using Kubernetes - Ben Hall = 1:00:36
m18QYJ66dSg = 5 years ago = HTTP: History & Performance - Ana Balica = 48:59
uRDRzJ6nWbc = 5 years ago = CSP XXP STS PKP CAA ETC OMG WTF BBQ… - Scott Helme = 1:03:38
yWVlsI56pA0 = 5 years ago = Going Solo: A Blueprint for Working for Yourself - Rob Conery = 51:47
LCj7h7ZoHA8 = 5 years ago = .NET Rocks Live with Jon Skeet and Bill Wagner – Two Nice C# People = 59:35
PBR5shDXVUI = 5 years ago = Hack Your Career - Troy Hunt = 1:01:26
ZyTLMnzehyU = 5 years ago = Building a Raspberry Pi Kubernetes Cluster and running .NET Core - Alex Ellis & Scott Hanselman = 1:00:45
k5r3Li_wqMo = 5 years ago = Probing the Mysteries of Saturn’s E-Ring with PostgreSQL - Rob Conery = 48:49
BOc9KiUuoU8 = 5 years ago = An Opinionated Approach to ASP.NET Core - Scott Allen = 58:48
SFLu6jZWXGs = 5 years ago = Building for Resiliency and Scale in the Cloud - Scott Allen = 51:24
v_lq5Od7EcA = 5 years ago = GitHub Beyond your Browser - Phil Haack = 52:36
6k7az23iZME = 5 years ago = An introduction to Kotlin by example - Dmitry Kandalov = 53:01
__0KqyluH_M = 5 years ago = The Power of Inclusion - Dennie Declercq = 52:07
qocp1cDxsuI = 5 years ago = Serverless in production, an experience report - Domas Lasauskas & Yan Cui = 1:02:27
vDe-4o8Uwl8 = 5 years ago = The Power of Composition - Scott Wlaschin = 1:00:57
wySnOo63y_A = 5 years ago = Beyond JavaScript Frameworks: Writing Reliable Web Apps With Elm - Erik Wendel = 54:28
ISSz344kJlU = 5 years ago = Go & Microservices - Matt Heath = 1:02:58
UNxhm89DwlY = 5 years ago = You build it, you run it (why developers should also be on call) - Chris O'Dell = 50:20
bgb2x7eKXY0 = 5 years ago = Simplifying Web App Development With Elm and Functional Programming - Ingar Almklov = 56:21
trHTLFNFoWk = 5 years ago = The History of .NET - Richard Campbell = 1:08:48
jHNqOlL2vOU = 5 years ago = Take Control of the Data of You - Nigel Parker = 1:03:45
tuVdq6Jnh_c = 5 years ago = Travel Guide to Software Systems - Patrick Kua = 51:52
ebfIsb7PQ1Q = 5 years ago = How to be a better interviewer, change the world and work with amazing people-Suzi Edwards Alexander = 1:02:02
E7mgufLJaOM = 5 years ago = Sondheim, Seurat and Software: finding art in code - Jon Skeet = 59:18
gjtFGx0yX5M = 5 years ago = Compositional UIs - the Microservices Last Mile - Jimmy Bogard = 1:01:37
RYI0DHoIVaA = 5 years ago = Diagnosing issues in ASP.NET Core Applications - David Fowler & Damian Edwards = 1:00:28
IF1aPR6da3A = 5 years ago = C# 7.1, and 7.2: The releases you didn't know you had - Bill Wagner = 1:01:29
q13g_Zef8nk = 5 years ago = C# 7 - Jon Skeet = 1:02:32
APUCMSPiNh4 = 5 years ago = Refactoring to Immutability - Kevlin Henney = 1:03:22
aSK8lGPgFgE = 5 years ago = I’m Pwned. You’re Pwned. We’re All Pwned. - Troy Hunt = 57:07
-a7JbXL0hq0 = 5 years ago = Implementing Authorization in Web Applications and APIs - Brock Allen & Dominick Baier = 57:42
ZTDZJGMMa_Q = 5 years ago = NDC Security Australia - Troy Hunt = 0:46
mXsLVZ76iks = 5 years ago = NDC Security Australia - Troy Hunt & Scott Helme = 1:41
yYC6gJ81Q9I = 5 years ago = WELCOME TO THE AGE OF CONVERSATIONAL INTERFACES! - Rabeb Othmani = 46:12
wFOT5u8JxW8 = 5 years ago = Make It Fixable - Patricia Aas = 43:38
2-pvOF6uTYQ = 5 years ago = Ionic, ngrx and Angular: building web and mobile apps with one code base - Duncan Hunter = 40:28
1IePuZzqosk = 5 years ago = Mötley Crüe and Mödern JavaScript - Eric Brandes = 45:14
jQCfeys4uaA = 5 years ago = Harnessing Chaos; the hidden ingredient behind building better systems - Russ Miles = 47:58
qugNNPXQfCs = 5 years ago = Why I’m Not Leaving .NET - Mark Rendle = 47:53
FKbykwvB_MU = 5 years ago = Cake + .NET Core = Write Once, Build Anywhere - Enrico Campidoglio = 1:12:13
jR3A0iZIz8c = 5 years ago = That's not in the User Manual: Unity3D Software and Hardware - Amie Dansby = 38:40
RdqDdMNzqU8 = 5 years ago = Who Needs Dashboards? - Jessica White = 41:39
qBMDqcO5vyA = 5 years ago = Starts with a search - Maria Naggaga = 46:27
Q8wMCTAGD88 = 5 years ago = Good Code: What, Why, and How to Get There - Jane Prusakova = 40:19
ji-WrWuhvrM = 5 years ago = Adventures in teaching the web - Jasmine Greenaway = 46:53
hdGmf3Fah-g = 5 years ago = The Developer’s Guide to Promoting Your Work - Todd Gardner = 44:30
u80GTmVtdG4 = 5 years ago = The power of technical decisions - Jake Ginnivan = 1:02:09
QYdOJ0QJptE = 5 years ago = API Gateway to Service Mesh: Navigating a Changing Landscape - Zhamak Dehghani = 39:08
TZzFPhVkzo4 = 5 years ago = IdentityServer for ASP.NET Core 2 - Brock Allen & Dominick Baier = 54:51
grr09e_cH_c = 5 years ago = Keynote: What is programming anyway? - Felienne = 1:06:11
HO0UKfx1LLA = 5 years ago = The Power ⚡️ and Responsibility 😓 of Unicode Adoption ✨ - Katie McLaughlin = 58:03
J60aPHTlALs = 5 years ago = ♫ These are a few of my favourite (Android) Things ♫ - Marcos Placona = 44:34
scZsv_mv0Bw = 5 years ago = CSP XXP STS PKP CAA ETC OMG WTF BBQ… - NDC Security 2018 = 1:00:56
bsiFUJSP3Zo = 5 years ago = Hear no evil, See no evil, Code no evil(); - NDC Security 2018 = 40:36
eyqUZ4uBC94 = 5 years ago = Hacking your neighbours and other life skills - NDC Security = 56:02
LVrL4Jmn_10 = 5 years ago = Adaptive Threat Modeling - NDC Security 2018 = 56:02
G4QyYiLlg5U = 5 years ago = ​Hacking Humans : Social Engineering Techniques and How to Protect Against Them = 46:45
Jh0G_A7iRac = 5 years ago = Secure Programming Practices in C++ - NDC Security 2018 = 51:35
Txt90iL-XzM = 5 years ago = I’m Pwned. You’re Pwned. We’re All Pwned. - NDC Security 2018 = 1:02:00
WEYTRb6BFsg = 5 years ago = Hack back - bug hunting on the dark side - NDC Security 2018 = 45:05
k12u-76CarE = 5 years ago = ​Beyond the OWASP Top 10 - Modern web application bugs - NDC Security 2018 = 47:02
HfXC3MSk9dY = 5 years ago = ​.NET Data Security : Hope is not a Strategy - NDC Security 2018 = 48:24
3p-iVgWItJ8 = 5 years ago = Data Distribution Service - Lars Ivar Miljeteig = 45:39
9e3lflYhNd8 = 5 years ago = Deliberate Architecture - Robert Smallshire = 43:58
k31wZafAMhk = 5 years ago = Design by Introspection - Andrei Alexandrescu = 47:33
s9dwdo700eQ = 5 years ago = The Holy Grail  - A Hash Array Mapped Trie for C++ - Phil Nash = 35:43
CsZDGlz7O5w = 5 years ago = Microservices and the Inverse Conway Manoeuvre - James Lewis = 46:51
eICYHA-eyXM = 5 years ago = C++ Performance and Optimisation -  Hubert Matthews = 43:48
oD6_bPlYkB4 = 5 years ago = Holograms of the Galaxy vol. 2 - Lars Klint = 46:01
s_50Vj_e05w = 5 years ago = There are Robots in my Bedroom - Introduction to Windows Mixed Reality - Lars Klint = 48:51
xGVRF-Y--hI = 5 years ago = History and Spirit of C - Olve Maudal = 42:01
yfgr00NL3zo = 5 years ago = Math, Juggling, Hidden Markov Models, and embedded Python - Jan Dyre Bjerknes = 40:02
v8aYNcE1QlI = 5 years ago = Threat modeling - Erlend Oftedal = 42:45
O7gUNNYjmsM = 5 years ago = Concurrent Programming in C++ - Venkat Subramaniam = 47:15
JWOCT6pVF70 = 5 years ago = Modern alternatives to make - Mike Long = 27:00
k0q_9YKB5ns = 5 years ago = Effective test scrubbing - Carl-Martin Rosenberg, Thomas Hanssen Nornes, Marius Liaaen = 49:32
Hpb9ByWqi3A = 5 years ago = Property based testing with Hypothesis - David R. MacIver = 49:32
yw7ZUaK7gY8 = 5 years ago = Seven Things Every Python Programmer Should Know - Robert Smallshire = 49:25
YwkAYXOrrrE = 5 years ago = 3D Printing for Software Developers - Nir Dobovizki = 50:52
mYzaFzAHuZ4 = 5 years ago = Fastware - Andrei Alexandrescu = 43:55
Xuqbl59f15A = 5 years ago = Keynote: The Art of Simplicity - Venkat Subramaniam = 41:07
uWoFC-AGr3g = 5 years ago = Debugging and Profiling .NET Core Apps on Linux - Sasha Goldshtein = 58:49
D_wwFYQ5Q1Q = 5 years ago = Blockchain is Cyberpunk - David Burela = 1:02:03
ajq6m1Ovw_o = 5 years ago = HTTP/2 - The future of the web today - Rob Crowley = 1:00:00
22CJNW_0sH4 = 5 years ago = Create a Consistent, Repeatable and Dependable DevOps process using FAKE - Has AlTaiar = 9:30
eBNtnKuuLRo = 5 years ago = .NET Data Security : Hope is not a Strategy - Stephen Haunts = 47:37
lH8h7s1_BDY = 5 years ago = Site Reliability 101 - Adrian Ubalde = 4:07
mwhOaB5VBwU = 5 years ago = F# Without Windows - Mitchell Tilbrook = 12:51
GyrOmXZS_5w = 5 years ago = Building Native Android Apps using React Native - Wei-Meng Lee = 1:05:25
N4sFhMD9acM = 5 years ago = #CANchangeratio - Women in Tech program to inspire more women into technology - Subha Chari = 14:38
esi8q_XPcBw = 5 years ago = Imposter Syndrome: Overcoming Self-Doubt in Success - Heather Downing = 46:26
oaYLfb61zGo = 5 years ago = Herding cats is easy compared to managing developers - Dom Millar = 9:48
62GNxqwOplQ = 5 years ago = Squashing JavaScript Bugs - Todd Gardner = 1:07:47
xENybGdaA6c = 5 years ago = When Feature flags go bad - Edith Harbaugh = 56:20
PN-iHYiQ8ZE = 5 years ago = Virtual reality for web developers - Alex Mackey = 53:21
9u6RgP2_n3c = 5 years ago = APIs with Microsoft Azure PaaS Services - Bill Chesnut = 1:00:42
HmGMbMBKTLw = 5 years ago = Service Workers - Patrick Kettner = 32:40
TKV7xLQuWf0 = 5 years ago = Take your ASP.NET apps to the next level with Google Cloud Platform - Mete Atamel = 57:44
tefBss-zA0Y = 5 years ago = Scaling Docker Containers using Kubernetes and Azure Container Service - Ben Hall = 1:04:04
LxEl7DN5uRg = 5 years ago = Developing Object Recognition for HoloLens - Stephen Carter = 58:49
tg_W-sNV0x8 = 5 years ago = Growing Serverless code with Azure Functions and F# - Mathias Brandewinder = 1:02:37
9VpAXOz3Kn8 = 5 years ago = Ionic, ngrx and Angular - Duncan Hunter & Adam Stephensen = 48:23
DpYICwCthOw = 5 years ago = Prescriptive Architecture Guidance for Cloud Applications - Mahesh Krishnan = 1:03:55
qw_Z5TyQIb8 = 5 years ago = Security And Microservices - Sam Newman = 52:33
9d7_4JXWtFY = 5 years ago = Hack Your Career - Troy Hunt = 59:22
F3GwkMI6XrM = 5 years ago = Web Apps can’t really do *that*, can they? - Steve Sanderson = 1:01:49
i7yoXqlg48M = 5 years ago = Docker, FROM scratch - Aaron Powell = 59:31
sq2mqeIG2I4 = 5 years ago = Life is like a Box of Chocolate(y) - David Gardiner = 52:19
VtUvk5jVQc4 = 5 years ago = Building a development environment out of your production deployment - Orin Thomas = 53:41
bda13k0vfc0 = 5 years ago = Asynchronous Programming From The Ground Up - Filip Ekberg = 59:29
rQ8MLh1EK54 = 5 years ago = The Code Behind The Vulnerability - Barry Dorrans = 57:40
Awc-RFs9HMs = 5 years ago = Accessing Accessible Accessibility - ​Jennifer Wong = 53:12
DW1PUpWil48 = 5 years ago = Choice is Overrated - Designing Products That Know What You Want Before You Do - Heather Wilde = 49:56
jGh5awmp_ZI = 5 years ago = Shipping Many Small React Components at Domain.com.au - Jess Telford = 1:04:00
mLX1sYVf-Xg = 5 years ago = Pushing C# to the limit - Joe Albahari = 57:29
r3kVwlr2I3U = 5 years ago = Confusion In The Land Of The Serverless: - Sam Newman = 51:42
yzqUut4x2s8 = 5 years ago = C# Language Internals - Bart De Smet = 59:56
HVHGah-r9dU = 5 years ago = From C# to Golang, My data science journey. - Julian Bright = 48:43
SpkiFTGzrkw = 5 years ago = Tales of a Unicorn Herder - Security in Startups and Disruptive Teams - Laura Bell = 44:39
TMaGvzBmnTU = 5 years ago = A lap around Microsoft Cognitive Services Vision API - Tim Huckaby = 1:00:06
fI1XGVIQjkA = 5 years ago = Writing high performance code in .NET - Bart De Smet = 1:02:12
n0dWcB0Y2HU = 5 years ago = Embracing Docker simplicity - while harnessing platform power - ​Michele Bustamante = 1:18:04
lqnUdEwVXOU = 5 years ago = Continuous Delivery in Azure - Jimmy Bogard = 1:03:06
slgZ8Dgfgno = 5 years ago = Profiling Node Applications - Sasha Goldshtein = 1:01:53
TRKEuYUajKA = 5 years ago = ASP.NET Core for Angular, React, and Knockout developers - Steve Sanderson = 1:01:42
IqWar6cEWsA = 5 years ago = The History of .NET - Richard Campbell = 54:03
WdZXrzuTxic = 5 years ago = How to start and run a software lifestyle business - Joe Albahari = 59:03
F-Lv-Q5GcCE = 5 years ago = Designing Wonderful .NET APIs - James Newton-King = 1:01:51
J_3_JFss1eg = 5 years ago = Microservices at Scale - ASP.NET Core, Service Fabric, and Azure in production - ​Louis DeJardin = 57:53
3fHSu04QwEw = 5 years ago = Where's my free lunch? - Hadi Hariri = 45:34
N7-SxDM9988 = 5 years ago = HoloLens Development: The Next Steps - Lars Klint = 1:00:55
PcHxmRI0ePo = 5 years ago = An Introduction Into Using Angular’s Material Design - Tracy Lee = 47:45
NMG_RFOZSlY = 5 years ago = What is React Fibre? - Jake Ginnivan = 48:16
361nnLIrnyY = 5 years ago = Deploying Applications as Containers on Windows Server 2016 - Ben Hall = 58:13
DxAGLC1ySNo = 5 years ago = Reverse Engineering a Bluetooth Lightbulb - Jesse Phelps = 45:39
pAPsqmBoWrY = 5 years ago = DevOps For Dishwashers - Bringing grown up practices to the Internet of Things - Christopher Biggs = 47:06
0gQNSevQVeo = 5 years ago = Machine Learning with F#, Redux - Mathias Brandewinder = 1:02:15
R8h0nuMAgBg = 5 years ago = Self-Aware Applications: Automatic Production Monitoring - Dina Goldshtein = 1:04:46
lTKhB6uAmno = 5 years ago = Techniques and practices for testing Angular - Duncan Hunter & Adam Stephensen = 55:49
7s1O9wuozeM = 5 years ago = Building Native iOS Apps using React Native - Wei-Meng Lee = 1:00:51
DBW284ZDSJ8 = 5 years ago = TensorFlow in Three Sentences - Barbara Fusinska = 58:36
IYIYw64eHH8 = 5 years ago = Building Docker Applications with .NET - Michele Bustamante = 1:06:11
Wd5EsgWQQRQ = 5 years ago = Transient Test Environments with Octopus - Robert Wagner = 41:37
duDlL9S1_kM = 5 years ago = "The website's down!" Stories and lessons on keeping your website up. - Adrian Ubalde = 24:31
1jwBSM0FkPg = 5 years ago = Software & the art of bicycle maintenance - Edith Harbaugh = 49:19
AAZhi3W6LOs = 5 years ago = Accessibility for UX: Don't worry, it's much worse than you think - Elle Waters = 59:29
Ol8gI4PF5pw = 5 years ago = How success can take you to the brink of failure: a case study - Vanessa Love = 48:00
jodafRC-TPE = 5 years ago = UX Patterns for Web Developers - Nicole Saidy & Jad Joubran = 48:34
rGAjN2mePSY = 5 years ago = The bold promise of teaching computers to understand the visual world - Tim Huckaby = 58:40
yyBijyCI5Sk = 5 years ago = Introduction to ASP.NET Core Razor Pages - Damian Edwards = 59:53
T1Ea5CY3f9A = 5 years ago = C#: Change, Openness, and Innovation - Bill Wagner = 54:29
nwGuSlmXavA = 5 years ago = Your Customers Hate You (And Other Lies) - Heather Wilde = 53:38
Z2Pcatq8tBs = 5 years ago = Implementing authorization in web applications and APIs - Dominick Baier = 1:01:50
NadXloUImDo = 5 years ago = A team's transition to Continuous Delivery - Ashley Noble = 1:00:46
zZAobExOMB0 = 5 years ago = Building AI Solutions with Google OR-Tools - Barry Stahl = 1:04:09
apk2pzubHH4 = 5 years ago = What can we learn from 750 billion GitHub events and 42 TB of code - Felipe Hoffa = 1:03:06
heRDuUtf8_o = 5 years ago = Elasticsearch: you know, for more than search - Russ Cam = 1:00:23
BcfHqBzVgDs = 5 years ago = Analyzing StackExchange data with Azure Data Lake - Tom Kerkhove = 59:28
qGqAhlFzkSU = 5 years ago = Data Cleansing With SQL And R - Kevin Feasel = 1:02:04
lZ2PKa_I528 = 5 years ago = Peanut Butter and Chocolate: Integrating Hadoop with SQL Server - Kevin Feasel = 59:28
QwFLbS47MSU = 5 years ago = Analyzing 33 million bike trips with BigQuery - Sara Robinson = 32:37
VZXkoc223qk = 5 years ago = Machine Learning and Big Data Magic with Node.js and Google Cloud - Sara Robinson & Bret McGowen = 58:33
fGmbXCrgKtg = 5 years ago = How to Tame a Penguin - Master Linux with ASP.NET Core - Brendan Richards = 55:35
srQt1NAHYC0 = 5 years ago = Functional Design Patterns - Scott Wlaschin = 1:05:50
RUozAfJc2sc = 5 years ago = Crappy to Happy: Strategies to Help You Kick Butt at Work - Kylie Hunt = 59:11
q4kNu8Oclew = 5 years ago = Building Resilient Applications In Microsoft Azure - Scott Allen = 1:00:00
0pJIApq9QFI = 5 years ago = UX design lessons from fighting games - Xharmagne Carandang = 14:06
ddrR440JtiA = 5 years ago = Simplified Unit Testing with the Entity Framework Core InMemory Provider - Jason Taylor = 14:45
f3pposukOSE = 5 years ago = Serilog: Instrumentation that Works for You - Nicholas Blumhardt = 59:06
yWaqR_-e4v4 = 5 years ago = The Power of Inclusion - Dennie Declercq = 36:29
wKQ8wuI61BI = 5 years ago = Congratulations, You're an Architect - Stephen Kennedy = 10:46
wuVptLrpWI4 = 5 years ago = Windows Subsystem for Linux - Jorge Arteiro = 10:36
ZDICBCNaBUw = 5 years ago = Gang up on difficult problems with Mob Programming - Jim Pelletier = 14:13
ksizv67V2Uk = 5 years ago = Running a Bug Bounty Program @ SEEK - Julian Berton = 56:20
T6d0T-gHeP8 = 5 years ago = Real world PowerBI - Matt Davies = 58:05
TfmBOzuPFLQ = 5 years ago = Security in ASP.NET Core 2.0 - Barry Dorrans = 1:01:10
bp6KEltdd9g = 5 years ago = Deep dive into building Bots with the Microsoft Bot Framework and Cognitive Services- Vishesh Oberoi = 59:43
c3Ciaz5X8FE = 5 years ago = Top Ten Worst Repositories to host on GitHub - Carlos Martín Nieto = 43:08
oL-m8yYlZAI = 5 years ago = Interactive C# Development with Roslyn - Filip W = 58:44
uOJ5MD835Jw = 5 years ago = Continuous Security - Laura Bell = 52:10
1pSH8kElmM4 = 5 years ago = Domain Modeling Made Functional - Scott Wlaschin = 51:35
GLfw0US7AhE = 5 years ago = The Art of Coding a Conversation: Designing Bots - Vishesh Oberoi = 49:56
XJTdZuRP0tc = 5 years ago = Take Control of the Data of You - Nigel Parker = 55:09
LGG3IIHUG_w = 5 years ago = Six Little Lines of Fail - Jimmy Bogard = 1:02:01
fPHkC9MsyYM = 5 years ago = Successful Code Sharing Principles for Mobile Development - Filip Ekberg = 57:12
7Gn0IcGCmQo = 5 years ago = Effective Eventual Consistency with Actor Models + Amazon Web Services - Philip Laureano = 42:51
ELemwZXJZVg = 5 years ago = An Introduction to NativeScript - John Bristowe = 46:33
YVqurfWzB-Q = 5 years ago = Hacking Humans : Social Engineering Techniques and How to Protect Against Them - Stephen Haunts = 40:53
p3_pVX2zsmg = 5 years ago = App deployment PaaS battle! - Matt Davies & Rob Moore = 1:00:01
wax4yE9JMbU = 5 years ago = Progressive what apps - Patrick Kettner = 39:10
CUdp1XGwRng = 5 years ago = Algebraic Data Types for C# - John Azariah = 1:03:10
Rl-KT-2OBew = 5 years ago = New Features in TypeScript 2 and beyond - Basarat Ali Syed = 1:00:14
4inY7TFEVT0 = 5 years ago = There is a better way - Geoffrey Huntley = 40:10
S9kxokKuFAQ = 5 years ago = Techniques in creating great cross platform apps. - Nigel Sampson = 54:09
CMx_2oIZwng = 5 years ago = Beyond Chatops: Bots @ Domain - Paul McManus = 10:46
NaByhM0KjAI = 5 years ago = Building for Alexa with Web API - Heather Downing = 57:17
Ta3N93ce5tQ = 5 years ago = How one team built their first microservice - Jim Pelletier = 54:14
VH0FIoFHB38 = 5 years ago = What the Functional? What, How and Why - Rob Howard = 50:57
Vz2lCUQTDvA = 5 years ago = Designing interfaces that don't suck when your customers scale! - Rob Pearson = 12:00
lzQfbTM-x0c = 5 years ago = Designing Voice User Interfaces for Amazon Alexa - Fabien Ruffin = 15:25
v9QGWbGppis = 5 years ago = Functional Programming Patterns for Mere Mortals - Daniel Chambers = 1:03:10
kJYHY_QcGwk = 5 years ago = Learning effective Kanban from your coffee shop - Dom Raniszewski = 10:14
0ghHBPNe6g4 = 5 years ago = Adventure in learning Go for a C# dev! - Ken Faulkner = 12:19
MOd6EjsauEw = 5 years ago = In Summary - Chris Hewitt = 9:28
_Ktn9ZbCx5E = 5 years ago = Chatbots - the next UI - Azadeh Khojandi & Jordan Knight = 58:50
KIiq8lIgUVk = 5 years ago = Building Data Intensive Microservices with Apache Kafka - ​Yaniv Rodenski = 58:51
vFvoylup874 = 5 years ago = Programming Robots – Making Friends with Cozmo - Lars Klint = 59:16
SwW00a9QCww = 5 years ago = Making Enabling Apps for disabled people - Dennie Declercq = 48:19
T42w0l1vghg = 5 years ago = Designing Great Progressive Web Apps - Nicole Saidy = 35:08
wJq86IXkFdQ = 5 years ago = Logic vs. side effects: functional goodness you don't hear about - Enrico Buonanno = 1:00:04
KB4y_BIbhx0 = 5 years ago = Using robots to test mobile apps - Sammy Connelly = 33:41
PgzTru5z0gk = 5 years ago = React Native Better Than Native - Mitchell Tilbrook = 54:25
nR_Ox_Y0Dfg = 5 years ago = 10 Things I learnt from my first HoloLens app - Hannes Nel = 1:02:24
4kwUC65QKdY = 5 years ago = The (Awesome) Future of Web Apps - Jad Joubran = 50:14
O-KmlUR5TgI = 5 years ago = Terraforming the world, one cloud at a time.  - Jeremy Cade = 1:02:36
PXPiN3ObFv8 = 5 years ago = The Technical Debt Prevention Clinic - Richard Banks = 1:01:12
TYjosLQ3yDE = 5 years ago = Redux, beyond React - Aaron Powell = 50:40
63k0Zc3yWb4 = 5 years ago = Keynote: Using EEG and Machine Learning to Perform Lie Detection - Jennifer Marsman = 1:00:31
Blo--Qio84w = 5 years ago = What’s new in ASP.NET Core 2.0 - Damian Edwards = 1:02:02
4F0B1GdqK5c = 5 years ago = What’s New in Visual Studio 2017 and VS Code - Adam Cogan = 1:02:32
S677jraR7Hs = 5 years ago = GraphQL - A query language to empower your API consumers - Rob Crowley = 1:00:01
jHU6Gl53FEs = 5 years ago = C# Scripting in the .NET Core world - Filip W = 58:36
o6aLNvlQaGo = 5 years ago = Keynote: Are There any Questions? - Dylan Beattie = 58:48
avFR_Af0KGk = 6 years ago = Web Application Security Risks: A Look at OWASP Top Ten 2017 - Christian Wenz = 59:34
CeAm6f_YzAU = 6 years ago = Building Resilient Applications In Microsoft Azure - Scott Allen = 59:28
D86wG5u-E14 = 6 years ago = The State of NoEstimates - Woody Zuill = 58:27
AfrqYM-qRHs = 6 years ago = The Future of Calling Microsoft APIs - Simon Jäger = 57:33
8qjNy8p_TnY = 6 years ago = Why I'm Not Leaving .NET - Mark Rendle = 49:46
J6qBzCVeMHo = 6 years ago = Accessibility for UX: Don't worry, it's much worse than you think - Elle Waters = 56:06
rHmIf5xmKQg = 6 years ago = Functional Techniques for C# - Kathleen Dollard = 58:10
jvdInWOlt3U = 6 years ago = Scaling Docker Containers using Kubernetes and Azure Container Service - Ben Hall = 1:02:33
MiLAE6HMr10 = 6 years ago = Web Apps can’t really do *that*, can they? - Steve Sanderson = 58:24
fxjywhxwYYU = 6 years ago = It's NDC - But Not As We Know It - Dylan Beattie & Mark Rendle = 1:04:48
SUHivewxa2I = 6 years ago = .NET Rocks Panel Discussion: Going Serverless = 45:56
Hlpn2Ov2rDk = 6 years ago = Building a Global App With Azure PaaS - Barry Luijbregts = 43:30
GzZKPxox9w0 = 6 years ago = What’s New in VS 2017 + VS Code - Adam Cogan = 1:03:21
Fuac__g928E = 6 years ago = Microservices and Rules Engines – a blast from the past - Udi Dahan = 52:48
kWU_LxYXMjE = 6 years ago = Composing high performance process workflows with Akka Streams - Vagif Abilov = 50:57
t4BC2IQLL_0 = 6 years ago = Data magic with the Elastic stack! - Aleksander Stensby = 1:00:38
d7Oy3rbxBak = 6 years ago = AB-tests, lies, damned lies, and statistics. - Emil Cardell = 52:04
94dS3kWDswk = 6 years ago = Going Serverless with GraphQL - Steve Faulkner = 33:40
wpXu6X_7xLM = 6 years ago = Handling secrets in kubernetes using git secrets - Tomas Jansson = 16:59
52vtO4h0tKU = 6 years ago = Serverless Cross-platform Apps with Xamarin.Forms and Google Firebase - Bjørn Egil Hansen = 16:25
ij08U1GGf90 = 6 years ago = Solving 5th grade math with F# and OCR - Martin Andersen = 10:08
FE2eoJFVqkw = 6 years ago = What’s new in ASP.NET Core 2.0 - Damian Edwards & David Fowler = 1:01:07
Bt7KzFxcbgc = 6 years ago = Fast and Small - What are the Costs of Language Features - Andreas Fertig = 56:59
kv8XedJTEww = 6 years ago = Visualise, document and explore your software architecture - Simon Brown = 1:00:03
PgZ2dxnj734 = 6 years ago = Serverless - reality or BS - notes from the trenches - Lynn Langit = 1:00:06
_l67mB_v-BM = 6 years ago = Becoming the bottleneck - Erlend Wiig = 28:44
8dvzgCcvdGY = 6 years ago = Building a Serverless, EventSourced Slack clone - Andy Davies = 55:53
QE6L3F-7img = 6 years ago = Suave – zero to hero of HTTP APIs - Henrik Feldt = 50:18
KPa8Yw_Navk = 6 years ago = F# for C# programmers - Scott Wlaschin = 1:00:01
1gfQFiGLZfw = 6 years ago = Creating A .NET Renaissance - Ian Cooper = 1:01:42
WDGP5pO1TyM = 6 years ago = C++17, part 1: The Language Features - Nicolai Josuttis = 59:53
EJeZ3YNnqz8 = 6 years ago = Implementing authorization in web applications and APIs - Dominick Baier & Brock Allen = 55:51
yEXJzRkq_Ug = 6 years ago = Stream Data Processing for Fun and Profit - David Ostrovsky = 1:01:19
atvgYJTBEF4 = 6 years ago = Efficient Time Series with PostgreSQL - Steve Simpson = 52:37
T025xQoDTHQ = 6 years ago = Inviting everyone to the party - Andrea Magnorsky = 35:37
sPseA_3UOMk = 6 years ago = Thinking in Events - Mathew McLoughlin = 54:04
3IUxyBx_PnM = 6 years ago = CSS Houdini - from CSS variables to JavaScript and back - Serg Hospodarets = 53:06
9sxfV67zCDE = 6 years ago = ASP.NET Core for Angular, React, and Knockout developers - Steve Sanderson = 58:36
BIkXid_pBiY = 6 years ago = Life, Liberty and the Pursuit of APIness : The Secret to Happy Code - Dylan Beattie = 56:55
G6IYBY-ZyLI = 6 years ago = C++ Performance and Optimisation - Hubert Matthews = 58:16
Up7LcbGZFuo = 6 years ago = Domain Modeling Made Functional - Scott Wlaschin = 51:39
PJT9D_4uUEg = 6 years ago = Easy Eventual Consistency with Actor Models + Amazon Web Services - Philip Laureano = 35:30
b1VFyEhucnA = 6 years ago = Azure Cosmos DB - The Best NoSQL Database You're Probably Not Using (Yet) - Josh Lane = 1:02:53
tc9CDdJmoWE = 6 years ago = Functional C++ for Fun & Profit - Phil Nash = 1:02:51
yj9GKRxFxVU = 6 years ago = C# 7 - Jon Skeet = 1:04:53
Fi2_Kfx3eE4 = 6 years ago = Paying taxes for fun and profit - Petter Hesselberg = 53:55
ORQ2qs8GHsQ = 6 years ago = I put 7 years of meal data in Datomic - Here's what I learned - Christian Johansen = 49:28
irvm5EdHQc0 = 6 years ago = Getting real(time) with Akka.NET, React and Redux - Francis Paulin = 43:28
sHWexPRFuUw = 6 years ago = Beyond JavaScript Frameworks: Writing Reliable Web Apps With Elm - Erik Wendel = 49:53
28ZAoStv-Xw = 6 years ago = When Feature flags go bad - Edith Harbaugh = 39:43
7qTOdbUAqno = 6 years ago = Feature Branches And Toggles In A Post-GitHub World - Sam Newman = 57:54
PZ44Y-Ch0AU = 6 years ago = Design principles and implementation strategies for better offline experience - Boyan Mihaylov = 44:02
DKPZgo_omwg = 6 years ago = Become a Visual Studio Ninja - Cecilia Wirén = 57:01
ZB0HtegKpic = 6 years ago = Cleaning the Sewage out of your DevOps Pipeline - Damian Brady = 1:00:37
qSrhVt0654U = 6 years ago = Working with C++ Legacy Code - Dror Helper = 48:47
_PEgl63V7wc = 6 years ago = C++17 part 2: The Library Features - Nicolai Josuttis = 1:02:53
vq8o_AFfHhE = 6 years ago = End-to-End Automated Testing in a Microservices Architecture - Emily Bache = 56:49
A2gYzEGQsS4 = 6 years ago = Domain Invariants & Property-Based Testing for the Masses - Romeu Moura = 56:34
pMMDVphop40 = 6 years ago = What CRDTs, distributed editing and the speed of light means to your writer friends- Jonathan Martin = 48:34
6HEpWGql-ak = 6 years ago = From Monolith to Serverless - Rajpal Wilkhu = 1:01:38
lsUgwfK9XIM = 6 years ago = Using C#'s Type System Effectively - Benjamin Hodgson = 1:01:42
F70NsQKGrGI = 6 years ago = "Doing Devops" as a politically powerless developer - Damian Brady = 1:01:07
Wcn-43roCgo = 6 years ago = Emerging Web Security Standards - Scott Helme = 42:58
TnDUbtXhGtM = 6 years ago = The Developer’s Guide to Promoting Themselves - Todd Gardner = 40:07
t-Pg1ZLjnak = 6 years ago = From zero to hero using Visual Studio Team Service - Anthony Borton = 59:15
45f0B1Bvpk8 = 6 years ago = Swift For The Curious - Phil Nash = 1:14:48
s-jqE_3rpzI = 6 years ago = Exploiting Relationship Graphs to Isolate Tenant Data - Dian Fay = 32:11
0VaZXbx55jo = 6 years ago = Investigating C++ Applications in Production on Linux and Windows - Sasha Goldshtein = 1:00:02
dATVOTBOl6c = 6 years ago = First Class Commands: The 2017 Edition - Reginald Braithwaite = 57:19
lcpQxcJAo4U = 6 years ago = What is .NET Standard? - Adam Ralph = 52:21
Jzs_sEyY5F4 = 6 years ago = Building for Alexa with Web API - Heather Downing = 54:50
YyQCZ2ib5uE = 6 years ago = Can you keep it a secret? - Lars Kristian Hagen = 10:25
ZNdpLM4uIpw = 6 years ago = ETW - Monitor Anything, Anytime, Anywhere - Dina Goldshtein = 57:30
fBUumVyafHw = 6 years ago = Security in ASP.NET Core 2.0 - Barry Dorrans = 58:18
vvQ-kK4coYM = 6 years ago = Using Trompeloeil - a mocking framework for modern C++ - Björn Fahller = 52:33
5HbM4SIHqGY = 6 years ago = Making magik - Josh Wulf & Prahlad Wulf = 11:59
KrAnFSKNBSI = 6 years ago = What To Expect When You Are Elixiring - Johnny Winn = 52:44
fBP18-taaNw = 6 years ago = Deep Dive into Git - Edward Thomson = 1:00:21
oaU1aiBuBRE = 6 years ago = Live Lambda Calculus - Einar W. Høst & Jonas Winje = 1:00:46
D2Vns3TSkC4 = 6 years ago = Debugging, Website Performance Issues & Real-Time Statistics - Hugo Cruz = 20:43
TqffpWalSUM = 6 years ago = Grain + Hops + IoT = Beer - David Christiansen = 13:38
zevgWcrR7jQ = 6 years ago = Skills vs Knowledge : are we learning the right things? - Natalia An = 12:00
Jw88UYVG9dg = 6 years ago = Debugging and Profiling .NET Core Apps on Linux - Sasha Goldshtein = 1:00:50
pabo99C6_JA = 6 years ago = Using F# on Azure Functions in Production - Nikolai Andersen = 57:30
5sEqLS65Rk8 = 6 years ago = Brave New .NET - Mark Rendle = 1:00:21
EiN3cF_y3vM = 6 years ago = C++ Unit testing - the good, the bad & the ugly - Dror Helper = 58:42
ivgad9ZI71Y = 6 years ago = Keeping the Noisy Neighbors Happy - Eran Stiller = 58:15
dGws1pMWzCI = 6 years ago = JavaScript in 2017: You might (not) need a framework - David Vujic = 44:14
rWkXaa01nFE = 6 years ago = .NET Blub: Frameworks beyond Microsoft - Joe Stead = 46:53
iRDcpkphrKs = 6 years ago = Conquer the JavaScript ecosystem with F# and Fable! - Alfonso Garcia-Caro = 1:01:06
tBkcX6eA63g = 6 years ago = Take Control of the Data of You - Nigel Parker = 1:00:00
8yeZI4WgygA = 6 years ago = Technology just killed the company - all hail the platforms - Jahn Arne Johnsen = 59:01
tR7HpDuVrEA = 6 years ago = Aurelia vs “just Angular” a.k.a “the framework formerly known as Angular 2” - Chris Klug = 58:40
_lqZnXWTNLY = 6 years ago = Visualisation - Gemma Cameron = 46:57
wJBJFHmidZA = 6 years ago = Everything You Always Wanted to Know About Azure Security But Were Afraid to Ask- Viktorija Almazova = 1:00:23
xzWJiHkLKaU = 6 years ago = Don't worry, your credit card details are safe. BTW your kid is missing! - Halvor Sakshaug = 55:51
CFn5I0c2uBE = 6 years ago = Abusing C# More - Jon Skeet = 1:01:41
K-1MpmwOlv4 = 6 years ago = Microservices and the Inverse Conway Manoeuvre - James Lewis = 1:00:06
zJVtpkxq_X0 = 6 years ago = Keeping it Simple With Go - Erik Engheim = 1:01:31
LVJCTlymUPw = 6 years ago = Betting on Performance: A note on Hypothesis-driven Performance Testing - James Lewis = 56:05
Ztoqv1LNDzc = 6 years ago = Develop Your Development Automation - Jessica Kerr = 58:50
CSPSvBeqJ9c = 6 years ago = State of the .NET Performance - Adam Sitnik = 56:20
H0IL7zZSLjg = 6 years ago = The secret weapon for developers, Notebooks. - Cristian Prieto = 54:13
CiXlVrbBepM = 6 years ago = How to stop worrying and love MSBuild - Daniel Plaisted = 1:02:02
jc7FpkyrOz0 = 6 years ago = Linux Security and How Web Browser Sandboxes Really Work - Patricia Aas = 49:50
5_z80eWpM4I = 6 years ago = Angular War Stories - Duncan Hunter & Adam Stephensen = 1:01:26
4nL1sW-u098 = 6 years ago = Crappy to Happy: Strategies to Help You Kick Butt at Work - Kylie Hunt = 48:49
Xe5-lXyCv2g = 6 years ago = The (Awesome) Future of Web Apps - Jad Joubran = 47:28
BnDbgmPIFf0 = 6 years ago = Successful Code Sharing Principles for Mobile Development - Filip Ekberg = 58:19
V7TrVwcU9T4 = 6 years ago = The Web lands in the Virtual and Mixed Realities - Maximiliano Firtman = 1:00:07
fmaPeUBWZuM = 6 years ago = Modern app development with Fable and React Native - Steffen Forkmann = 1:03:14
CH9VEeV-zok = 6 years ago = An Opinionated, Maintainable REST API Architecture for ASP.NET Core - Spencer Schneidenbach = 49:28
d-0TxC0GiUQ = 6 years ago = Getting Started with Electron - Brendan Forster = 47:50
-dUAu-ztGcA = 6 years ago = Something Something Cyber - Troy Hunt = 1:01:24
R20yMPli2KM = 6 years ago = Designing great progressive web apps - Nicole Saidy = 38:56
5kt3urZOg4g = 6 years ago = Flow - Am I Your Type? - Mark Volkmann = 58:10
LY9DdlQ6v3k = 6 years ago = Taming the Web with Cowboy & Coyote - Johnny Winn = 38:46
JQsyc-aa5q4 = 6 years ago = Building big teams with Nexus - Martin Hinshelwood = 1:04:01
A7aAw2ry7CY = 6 years ago = Analyzing 33 million bike trips with BigQuery - Sara Robinson = 29:46
Q-r9MXZYut4 = 6 years ago = Azure Functions and Microsoft Cognitive Services Computer Vision API - Todd Fine = 1:00:29
MXjphW6j7do = 6 years ago = ARM FTW – Azure Resource Manager For The Win - Magnus Mårtensson = 55:25
NVolBae9fKI = 6 years ago = User Experience at Every Level of Business - Christina Aldan = 42:55
e1NqkrAL4Ro = 6 years ago = Terraform - colonising Azure! - Stefan Magnus Landrø = 1:00:00
0JzTNSTqMGY = 6 years ago = Dynamic Teams - Fluidity for the win - Doc Norton = 1:00:12
BQE8HmD7-vk = 6 years ago = Beyond step-by step debugging in Visual Studio - Tess Ferrandez = 1:01:17
UgBhRKySass = 6 years ago = Building Connected & Disconnected Mobile Apps - James Montemagno = 1:01:26
CrS0HVQZiQI = 6 years ago = Confusion In The Land Of The Serverless: - Sam Newman = 55:20
QcHJl7DNaHI = 6 years ago = Goodbye history tables, hello full audit- exploring message streams & event sourcing- M. Bustamante = 1:04:36
_dlKELBYgrw = 6 years ago = The blockchain: what, why and how - Benny Michielsen & Hans Peeters = 57:06
-MUhcgXBj_A = 6 years ago = Hack Your Career - Troy Hunt = 58:52
QwgQulAOY0Q = 6 years ago = Sensors, data and dashboards: Azure IoT end-to-end - Martin Abbott = 56:43
eDyLeb3rqqI = 6 years ago = Imposter Syndrome: Overcoming Self-Doubt in Success - Heather Downing = 47:28
uO3a4HIBDU4 = 6 years ago = Programming is writing is programming - Felienne = 55:47
SE4VoErp134 = 6 years ago = Beautiful apps with Fuse using your XAML and JavaScript skills - Christer Veland Aas = 56:44
XtvMt6A4JZw = 6 years ago = Real-time surveillance of potential epidemics-Einar Ingebrigtsen, Tonje Tingberg & ​Richard Campbell = 1:01:06
LaLUQFFvtDY = 6 years ago = AWS Serverless with .NET Core - Norm Johanson = 49:44
Sh-kRv9Yemg = 6 years ago = Keep you data safe in a containerized application - Hagai Barel = 48:47
OhmNp8UPEEg = 6 years ago = Serilog: Instrumentation that Works for You - Nicholas Blumhardt = 53:36
V1hpp-7ZNjY = 6 years ago = Visual Studio Mobile Center: Fast and Fun Continuous Delivery for Mobile apps - Karl Krukow = 53:45
iKi0dhA9-Go = 6 years ago = Scaling Serverless F# with Azure Functions - Mathias Brandewinder = 1:01:49
EcGH6hQxY8A = 6 years ago = Banish Your Inner Critic v2.0 - Denise Jacobs = 1:11:35
k-eU8_-174g = 6 years ago = ABC of CSS3 animations - Ronald Mavarez = 8:59
8ilow_2Ayos = 6 years ago = Making apps with React Native - Christian Brevik = 14:10
eFl1EMbbp8M = 6 years ago = Become an SVG Architect, not a PowerPoint Architect! - Filip van Laenen = 7:08
jTBmmOECkJ4 = 6 years ago = A Vue to A Kill - an introduction to Vue.js - Andreas Ahlgren = 13:56
0nN9NuGkxEE = 6 years ago = React components, atomic design and storybook - Einar Afiouni = 6:51
c5wodlqGK-M = 6 years ago = Coroutine Concurrency in Python 3 with asyncio - Robert Smallshire = 1:00:29
8WrjthKFbTw = 6 years ago = Compositional UIs - the Microservices Last Mile - Jimmy Bogard = 56:01
jbOflGXBQao = 6 years ago = Cancer Genomics - a biologist and a developer - Samantha Langit & Lynn Langit = 49:58
o2hSImNYXR0 = 6 years ago = #ToyFail: Is your child safe from the Internet of Things? - Martin Gravåk & Kristian Wille = 46:31
3mipYw5lFtU = 6 years ago = FAKE + Paket – PowerTools for .NET developers - Steffen Forkmann = 1:04:12
D0kDqr6FUWQ = 6 years ago = Microservices with Service Fabric. Easy... or is it? - Daniel Marbach = 1:07:32
12pAP5XLuI8 = 6 years ago = HoloLens Development: The Next Steps - Lars Klint = 59:18
GVO09zcFNtY = 6 years ago = Microservice Swarms: Decentralized Discovery and Scaling - Allen Holub = 59:14
J3vIW71W_2w = 6 years ago = Adopting open source in your organization - Edward Thomson = 57:59
iItGjh6dz9E = 6 years ago = Better: Fearless Feedback for Software Teams - Erika Carlson = 46:11
iUkgBfBrnmA = 6 years ago = Extending and Optimizing Xamarin.Forms Mobile Apps - James Montemagno = 1:03:51
BhTbOtuSUzQ = 6 years ago = It's not your parents' HTTP - Gleb Bahmutov = 58:40
BmZhSS40yAM = 6 years ago = Building a Serverless API With Google, Firebase and PostgreSQL - Rob Conery = 50:07
M-QXYLygo2M = 6 years ago = ReST 3.0 – A lap around HTTP Apis' next generation - Sebastien Lambla = 57:52
opf7xX-whIw = 6 years ago = JavaScript Metaprogramming - ES6 Proxy Use and Abuse - Eirik Langholm Vullum = 51:49
qxeOo2jWoNM = 6 years ago = Practical Empathy: Unlock the Super Power - Pavneet Singh Saund = 43:36
MBLgP82uchg = 6 years ago = The Hybrid Docker Swarm: Mashing Windows and Linux Apps with Containers - Elton Stoneman = 44:38
og_oE5JX8_0 = 6 years ago = Multi-container applications with .NET Core on Kubernetes - Magnus Stuhr & Ståle Heitmann = 57:50
jqXElfRRobM = 6 years ago = Open Source Software Foundations: Not Totally Boring, Actually Super Awesome - Jon Galloway = 57:01
3rtq8M1s95c = 6 years ago = Identity Server 4 with Angular and ASP.NET Core - Ben Cull = 1:02:36
dw6wJMqzl2Y = 6 years ago = Scaling Agile in your Organization with the Spotify Model - Stephen Haunts = 46:25
UTgxdcADGa0 = 6 years ago = Servant: Web APIs at the Type Level - Erlend Hamberg = 23:56
KoSSlxjTdXk = 6 years ago = Goodbye REST; Hello GraphQL - Sandeep Singh = 58:51
WTdPup__4LY = 6 years ago = Sex Robots - Kate Devlin = 55:06
I9SqEvUOAoM = 6 years ago = Badass 101 - Lyndsey Padget = 46:03
jMhr4bb2oOU = 6 years ago = The state of IoT in 2017 and how Norwegian Technology make IoT Easy - Joakim Lindh = 46:23
Zh_2OHgYdvg = 6 years ago = Optimism and the Growth Mindset - Reginald Braithwaite = 58:01
ka_horV66As = 6 years ago = Building ASP.NET apps on Google Cloud - Mete Atamel = 51:45
2S3Jxg9Ba9A = 6 years ago = Ben Cull Beer Research = 1:20
deageBBNm0k = 6 years ago = Ben Cull - NDC Oslo 2017 Beer Ølsmia = 3:56
Tr5o3bPjaxM = 6 years ago = C# Scripting in the .NET Core world - Filip W = 57:42
ZQjRga_LLas = 6 years ago = Where’s my free lunch? - Hadi Hariri = 33:01
fA7gA1Bg8H8 = 6 years ago = Serverless Compute with Azure Functions - Magnus Mårtensson = 59:02
lwyqqrzZcTE = 6 years ago = Big Scrum: Scaling Scrum with Nexus - Martin Hinshelwood = 58:53
05g7Yz7I6aM = 6 years ago = Launching patterns for containers - it's more than just scheduling - Michele Bustamante = 1:03:32
H4gvrDFmrsQ = 6 years ago = Patterns for scalability and availability in (trading) systems - Michel André = 1:05:41
_EZJmrgZYpc = 6 years ago = Agile Experiments in Machine Learning with F# - Mathias Brandewinder = 58:13
szILg-hyFUQ = 6 years ago = An Opinionated Approach to Using ASP.NET Core - Scott Allen = 1:00:58
TLm-i5sVlNM = 6 years ago = Pushing it to the edge - Eirik Vullum = 44:58
OwRzz0rUU2U = 6 years ago = Message Brokers and Containers - the new ESB is “no ESB” - Michele Bustamante = 54:59
l7MgGY3lnts = 6 years ago = IdentityServer4: New & Improved for ASP.NET Core - Dominick Baier = 1:00:15
K6NAamhupmE = 6 years ago = There Be Dragons in the New JavaScript - Scott Allen = 52:47
lSLTwWqTbKQ = 6 years ago = Taking Elixir to the Metal with Rust - Sonny Scroggin = 45:42
t916ikik6W0 = 6 years ago = Serverless F# with Azure Functions: fsibot goes nano-services - Mathias Brandewinder = 1:02:07
0OTPTNJji1I = 6 years ago = Collaborative Music with Elm and Phoenix - Josh Adams = 50:04
o4-CwDo2zpg = 6 years ago = Fastware - Andrei Alexandrescu = 1:00:00
WsgW4HJXEAg = 6 years ago = Three Unlikely Successful Features of D -  Andrei Alexandrescu = 1:00:51
nNSdzb-_8_s = 6 years ago = Mobile DevOps with Xamarin and Visual Studio Team Service  - Richard Erwin = 1:03:48
f5TWQq_A4_0 = 6 years ago = Machine Learning for Muggles -  Martin Kearn = 1:02:56
a-yQEBvLARo = 6 years ago = Building Connected Azure Apps with Xamarin - Richard Hopkins & Mike James = 59:51
uBgqyknGA-0 = 6 years ago = Microsoft Cognitive Services: Making AI Easy - Jennifer Marsman = 1:05:13
j4fKFKh2vmI = 6 years ago = Next Generation Asynchronous Patterns in JavaScript - Jonathan Mills = 44:59
rTVLJlHeet4 = 6 years ago = Techniques and practices for testing Angular 2 - Duncan Hunter and Adam Stephensen = 59:15
SVouWfoHhk0 = 6 years ago = Go, Microservices and all the joy! - Andrzej Grzesik = 45:07
grolmPjW3D0 = 6 years ago = Chatbots: The hype, challenges and opportunities - Galiya Warrier = 53:44
Rjy3W5LqBeM = 6 years ago = Branching Out with Elm - Dave Fancher = 56:42
M9xk7KkSY1A = 6 years ago = Visualizing Olympic Medals with F# and Fable - Tomas Petricek = 59:53
NpVvQXEbs2M = 6 years ago = The (Awesome) Future of Web Apps - Jad Joubran = 54:51
G13IWuA_7_Y = 6 years ago = Writing better tests for your JavaScript app - Jake Ginnivan = 1:01:42
rWXzOIvNSws = 6 years ago = The Victorian Age of JavaScript - Eric Brandes = 47:58
gXQTthPIxKg = 6 years ago = Where did you find that? - Niall Merrigan = 57:36
tutHpyz05xw = 6 years ago = Applying Agile Thinking: Run Measure Learn - Julia Mitchelmore = 42:25
S-jiM07X3fs = 6 years ago = Deep .NET Debugging - Tess Ferrandez = 52:52
Fe8FrjHHxJQ = 6 years ago = Of Elephants, Mooses and other problems in the Room -  Sabine Wojcieszak = 47:33
dN46VlQnJ_8 = 6 years ago = Predicting the future as a service with Azure ML and R - Barbara Fusinska = 58:46
KdVwmph7HDk = 6 years ago = Enhanced AML fraud detection solutions with Azure Machine Learning - Ravi Kanth = 49:10
knr_5sxBi7A = 6 years ago = High Tech Delight - Programming the 'Hard' out of Hardware - Suz Hinton = 50:57
BnnFygfVLOI = 6 years ago = Neural networks by example - Natalia An & Katya Mustafina = 54:27
NgERP5g_Nuw = 6 years ago = Scaling applications with Azure Redis Cache and Machine Learning - Stefano Tempesta = 1:01:02
rqQVmot_Fag = 6 years ago = Chatbots: The hype, challenges and opportunities - Galiya Warrier = 35:07
rhSB8uECvfs = 6 years ago = DevOps and Agility with Visual Studio, Azure and Scrum - Martin Hinshelwood = 53:22
-ozKx_EzLCg = 6 years ago = Focus on the User: Making the World a Better Place -  Jeremy Clark = 56:00
sabcJ1u1e-M = 6 years ago = Deploying Applications to Windows Containers and Windows Server 2016 - Ben Hall = 1:02:15
c3M4Navs-jY = 6 years ago = Monitor your containers with the Elastic Stack - Philipp Krenn = 59:32
HQJI_33CWao = 6 years ago = Brownfields DevOps in Practice - Damian Brady = 55:53
VBFcx2jXuJY = 6 years ago = Real world DevOps with the Microsoft ALM Rangers - Wouter de Kort = 52:51
iki4Of176MU = 6 years ago = The .NET standards for Dummies - Matt Ellis = 53:09
nw4DBBFilBY = 6 years ago = The Velvet Revolution: Dockerizing Legacy ASP.NET Apps - Elton Stoneman = 1:00:50
GzKC4juJB48 = 6 years ago = The Async Arrow - Troy Kershaw = 52:30
Sj9E_10K4Pw = 6 years ago = Get Reactive with RxJS -  Venkat Subramaniam = 1:01:25
RCFEGFcXAy0 = 6 years ago = Software Engineering ​: Greatest Hits 1947   2047   Mark Rendle & Dylan Beattie = 52:17
gVXEwfH6FLc = 6 years ago = Something Something Security  - Troy Hunt = 56:48
_CWpwTymxDI = 6 years ago = So many Docker platforms, so little time... - Michele Bustamante = 1:06:15
2qf05XALZXo = 6 years ago = Exploring Pattern Matching in C# - Bill Wagner = 55:03
Ym9nhVZs89o = 6 years ago = Visualise, document and explore your software architecture -  Simon Brown = 57:26
-7WRQFclEA8 = 6 years ago = Using EEG and Azure Machine Learning to Perform Lie Detection - Jennifer Marsman = 1:05:19
FUkfaeiCi8w = 6 years ago = Doing I.T. for SCIENCE! - Sprints, Startups and the Scientific Method - Dylan Beattie = 46:56
daD_qwPR3SA = 6 years ago = The Tension Between Expediency and Correctness - Josh Adams = 46:42
-Ig-RoWzzJ8 = 6 years ago = Exploring StackOverflow data - Evelina Gabasova = 54:43
ELwTKHiKZS4 = 6 years ago = C++17: The Library Features - Nicolai Josuttis = 56:28
_g4am_bLJUs = 6 years ago = Taming Cloud Complexity with F# DSLs - Yan Cui = 42:34
pY-_93cfvso = 6 years ago = The C++ Type System is your Friend - Hubert Matthews = 50:32
O-x5GPTJBz0 = 6 years ago = Responsive Web Design for Developers with Visual Studio - Don Wibier = 59:20
pEzV32yRu4U = 6 years ago = C++17:  The Language Features - Nicolai Josuttis = 1:01:50
cxs7oLGrxQ4 = 6 years ago = From Dependency injection to dependency rejection - Mark Seemann = 59:39
ntWdmlrCheY = 6 years ago = Let’s Get Lazy—The Real Power of Functional Programming - Venkat Subramaniam = 58:14
b6FFY9-Q9Uw = 6 years ago = Squashing JavaScript bugs  - Todd H. Gardner = 57:31
QMT-EQQ5ge4 = 6 years ago = TypeScript – JavaScript for C# devs - Chris Klug = 1:02:47
gfh-VCTwMw8 = 6 years ago = Avoiding Microservice Megadisasters - Jimmy Bogard = 45:27
8YtjEalqB2U = 6 years ago = Conversations for the masses - Peter Drougge = 54:57
dbyQynY7zDw = 6 years ago = Redux, beyond React - Aaron Powell = 48:45
Wh9VLDY6vR4 = 6 years ago = UX Patterns for Developers - Nicole Saidy and Jad Joubran = 45:30
2aUAqnKegQQ = 6 years ago = Punishment Driven Development - Louise Elliot = 53:20
0q2McQR7tM8 = 6 years ago = Lean accessibility: Building inclusive design into your agile workflow - Elle Waters = 53:43
QWHEP4fCmX4 = 6 years ago = Feed the links, tuples' a bag – Intro to Linked Data APIs - Sebastien Lambla = 33:36
BBbmFMF8DlA = 6 years ago = C#7 and Visual Studio 2017 - Kathleen Dollard = 59:11
JP-BLyD59uw = 6 years ago = Aurelia: Next Generation Web Apps - Ashley M Grant = 56:11
cQ5qF9PmyCQ = 6 years ago = Get Func-y: Delegates in .NET - Jeremy Clark = 59:28
EH07FhUsn8A = 6 years ago = There's a Hologram in my UI! - Jessica Engström = 50:48
OF8cxc5w4A8 = 6 years ago = Angular 2 War Stories - Duncan Hunter &  Adam Stephensen = 58:05
DzRI1L7z9o0 = 6 years ago = The Afterlife: Languages after JavaScript - Jennifer Wong = 35:56
DkG76TgntBQ = 6 years ago = Consolidating Services With Middleware - Christian Horsdal = 1:00:01
vecVMhdR-kw = 6 years ago = Using AWS Lambda and Azure Functions to develop serverless applications - Rajpal Singh Wilkhu = 1:08:07
dmvorUUuaX8 = 6 years ago = Fonts, Form and Function: A Primer on Digital Typography - Robby Ingebretsen = 1:03:17
XBC0vDO4yCk = 6 years ago = Squeezing the Hardware to Make Performance Juice - Sasha Goldshtein = 1:01:47
G49baWvzCOI = 6 years ago = Look Mommy, No GC! - Dina Goldshtein = 1:05:02
qiqLhlG4CkU = 6 years ago = What are Graph Databases and Why should I care? - Dave Bechberger = 56:05
WJLVLd3Zy1Q = 6 years ago = Web Application Security: Browsers Fight Back! - Christian Wenz = 55:20
CwGGl4dx2yQ = 6 years ago = Node.js Security - Ilya Verbitskiy = 55:51
HZ3sYta9yrg = 6 years ago = Broken Crypto is Broken - Erlend Oftedal = 53:53
M-UcUs7IMIM = 6 years ago = Get to grips with asyncio in Python 3 - Robert Smallshire = 59:23
_MLpZZBD-ps = 6 years ago = Hacking Humans - Stephen Haunts = 55:14
iJXgObpYAtY = 6 years ago = Agile in a Business to Business relationship - Camilla Brown = 50:33
esOmLqp6YuE = 6 years ago = How to go from opening Visual Studio to interacting with a live chat bot in 10 minutes = 10:04
N0MtHdIhJlU = 6 years ago = Testing in Python - Austin Bingham = 59:15
VorG4K_5gfw = 6 years ago = self.improve(): Building a Technical Career - Erika Carlson = 56:24
lGhfyA7aZSc = 6 years ago = A world of devices - Laurent Bugnion = 58:47
ewiEeWUqo14 = 6 years ago = Holographic Programming – Exploring the HoloLens - Lars Klint = 59:11
J5U6LxnjYy4 = 6 years ago = Engineering for Engineering's Sake - Mindaugas Mozūras = 44:23
x0yNKU-tz1Y = 6 years ago = Never RESTing – RESTful API Best Practices using ASP.NET Web API - Spencer Schneidenbach = 1:00:37
X9dFBt31UVw = 6 years ago = An independent look at the arc of .NET - Kathleen Dollard = 1:02:56
vIg_rrAxulo = 6 years ago = Build Your Own Azure - Mark Rendle = 1:01:18
uD5D8geeQjY = 6 years ago = Bundling your Front-End with webpack - Sandeep Singh = 16:30
wADPwtJcy20 = 6 years ago = .NET Rocks Live Panel on Machine Learning = 1:00:36
5cvaCq1q9_E = 6 years ago = Mob Programming, A Whole Team Approach -  Woody Zuill = 59:34
JIlO_EebEQI = 6 years ago = Abusing C# - Jon Skeet = 1:02:16
99Zacm7SsWQ = 6 years ago = The Post JavaScript Apocalypse  - Douglas Crockford = 54:13
lVezcdfjWis = 6 years ago = The Seif Project   Douglas Crockford = 45:00
saeKBuPewcU = 6 years ago = Working with Time is Easy   Jon Skeet = 1:04:43
KZRfW4mgtMM = 6 years ago = Make Cyber Great Again - Troy Hunt = 23:07
-g8l7ghg7uQ = 6 years ago = This Is My 10-Year-Plan. What's yours? - Mark Rendle = 57:02
fBFLCP06vyA = 6 years ago = Troy Hunt on his "Hack yourself first" workshop = 1:00
lPL9OYLoOEc = 6 years ago = Bundling your Front-End with webpack - Sandeep Singh = 16:30
KqbJbJOJtVI = 6 years ago = Web apps that talk - Ilya Verbitskiy = 9:16
YNQfK4foSrA = 6 years ago = Remixing my career - João Lebre = 16:57
zULU6Hhp42w = 6 years ago = Better Code: Concurrency - Sean Parent = 1:07:36
QGcVXgEVMJg = 6 years ago = Better Code: Runtime Polymorphism - Sean Parent = 57:33
FyCYva9DhsI = 6 years ago = Clean Coders Hate What Happens to Your Code When You Use These Enterprise Programming Tricks = 1:11:23
mlkE8EJZODw = 6 years ago = Functional C++ - Kevlin Henney = 1:01:01
BzSAXSxytpQ = 6 years ago = Getting the best out of ASP.NET Core in Azure - Jon Galloway = 1:01:45
q-ddUwXo12A = 6 years ago = How to Break TypeScript (and How to Put it Back Together) - Benjamin Hodgson = 11:59
2yXtZ8x7TXw = 6 years ago = Thinking Outside the Synchronisation Quadrant - Kevlin Henney = 1:07:43
Ah13fl6VZag = 6 years ago = How to get your submission accepted at NDC London - Chris O'Dell = 10:53
hO7mzO83N1Q = 6 years ago = JavaScript Patterns for 2017  - Scott Allen = 56:03
f5uGoUmNgl8 = 6 years ago = Becoming an awesome open source contributor - Christos Matskas = 10:17
x4tIKIhGz2U = 6 years ago = 0-60 in the .NET Framework - Software development for Formula 1 - Chris Alexander = 1:08:19
MmL8H0oGGe8 = 6 years ago = Ops and Operability - Dan North = 49:25
Al8LrBKpZEU = 6 years ago = Back to Basics: Efficient Async and Await - Filip Ekberg = 57:03
eF2myGRT8bo = 6 years ago = Building JavaScript and mobile/native Clients for Token-based Architectures = 57:43
rYlwiJ0vr_4 = 6 years ago = How Complexity Theory Can Save Your Job - Rob Conery = 48:09
i2gEbw_jzfY = 6 years ago = Migrating to Serverless - an experience report - Gojko Adzic = 1:03:55
VBgMb53d2ik = 6 years ago = The Zen of Powershell - PowerShell for the C# dev - Peter Ibbotson = 1:03:26
AgnUu0y6A88 = 6 years ago = The Force Awakens - Mastering Your Inner Developer - Lars Klint = 1:01:57
5b7qNYCrHWg = 6 years ago = Web Performance Deep Dive - Chander Dhall = 1:01:25
JjFfC1zhsOA = 6 years ago = Why User Data is about more than Forms - Chad Gowler = 41:41
uamh7xppO3E = 6 years ago = Microservices and the Inverse Conway Manoeuvre - James Lewis = 57:58
GzYkO6cJ1DA = 6 years ago = Twelve Factor Apps in .NET : Building apps for the cloud - Ian Cooper = 1:11:06
EZtZxBm5esc = 6 years ago = Delivering Unicorns -  Kasia Mrowca = 56:51
oSr2VRxromk = 6 years ago = Data + Docker = Disconbobulating? - Stephanie Locke = 1:00:29
9a1PqwFrMP0 = 6 years ago = An Introduction to CQRS and Event Sourcing Patterns - Mathew McLoughlin = 50:08
AG3KuqDbmhM = 6 years ago = Thirteen ways of looking at a Turtle -  Scott Wlaschin = 1:04:42
F-7MX_Az6_4 = 6 years ago = Phoenix: an Intro to Elixir's Web Framework - Sonny Scroggin = 1:00:22
fCsAUnfCmDE = 6 years ago = VSCode: Tips and Tricks - Sahil Malik = 56:37
eQzF8RrLM6s = 6 years ago = The Book of F# - Dave Fancher = 1:02:05
7OVU9Mqqzgs = 6 years ago = How to build real-world applications with Orleans - John Azariah and Sergey Bykov = 1:01:24
IJPa8ZUoztc = 6 years ago = Becoming an awesome open source contributor - Christos Matskas = 53:17
YPGuguXiBes = 6 years ago = Using Terraform and Consul to delegate service deployment to service teams - James Nugent = 53:38
8nFYg_KkKrE = 6 years ago = Cloud nano-bots: Strongly-Typed State Machines In The Cloud - John Azariah = 52:50
uJOGeyQIbpc = 6 years ago = The beauty of stupid ideas - Aaron Powell = 53:50
KQwskUjsSi8 = 6 years ago = Life with actors: experience report - Vagif Abilov and Erlend Wiig = 58:13
QxKHi1wFBfc = 6 years ago = Debugging your website with Fiddler and Chrome Developer tools - Robert Boedigheimer = 59:52
gjFOd_z42uM = 6 years ago = Building Fast and Beautiful apps with Xamarin.Forms - Michael Ridland = 58:25
6nn5o1-2FaI = 6 years ago = Building a real-world cross-platform app with Xamarin and MVVM - Gill Cleeren = 1:01:12
HLs6WgAmX64 = 6 years ago = Pipe forward : Using Elixir and F# together - Bryan Hunter = 1:06:32
qDE8NYQedKI = 6 years ago = How to Scale .NET Apps with Distributed Caching- Iqbal Khan = 1:02:22
c9O5_a50aOQ = 6 years ago = Elasticsearch Do's, Don'ts and Pro-Tips  - Itamar Syn Hershko = 1:01:09
KZYHdYKEa5Q = 6 years ago = ARM FTW  Magnus Mårtensson = 1:00:39
bQJLQ14beNk = 6 years ago = Serverless Architecture - Tales from a world without servers - Robin Weston = 1:00:02
x-C-CNBVTaY = 6 years ago = Patterns for application development with ASP.NET Core - Damian Edwards & David Fowler = 1:02:13
wIsync6vTfQ = 6 years ago = Introducing ASP.NET Core Sockets - Damian Edwards & David Fowler = 1:02:02
PhRFLKtJcSs = 6 years ago = What were they thinking? Language design choices that seem wrong, until they don't. - Bill Wagner = 1:00:04
TBtQqwyx-Fo = 6 years ago = Head to Head: Jon Skeet, Kathleen Dollard and Rob Conery = 1:00:12
YXdJ2HLAOdE = 6 years ago = IdentityServer4: New & Improved for ASP.NET Core - Brock Allen & Dominick Baier = 58:07
6Fi5dRVxOvc = 6 years ago = An Opinionated Approach to ASP.NET Core - Scott Allen = 55:49
Z4wyg00QHN0 = 6 years ago = NDC London 2017 Keynote: Saving the World One App at a Time – Richard Campbell = 32:58
opMZrAUAstw = 6 years ago = NDC - Inspiring Software Developers Since 2008 = 1:07
ErWDWEmJNQw = 6 years ago = Machine Learning with Functional Programming Workshop -  Mathias Brandewinder = 0:59
pwhmYvWIpBs = 6 years ago = AngularJS 2.0 Workshop with Duncan Hunter and Adam Stephensen = 0:29
GNByrg8lx68 = 6 years ago = Dominick Baier - Identity & Access Control for modern Web Applications and API = 1:04
TjZxCu8iVSk = 6 years ago = NDC London 2017  - Jennifer Marsman on EEG and Azure Machine Learning to perform lie detection = 1:07
CZMEGEdLpBA = 6 years ago = NDC London 2017- Day 1 with Bill Wagner = 0:36
Qcdwe46nJW8 = 6 years ago = How to defeat feature gluttony  - Kasia Mrowca = 1:03:16
-S1gogAJioM = 6 years ago = Performance & Stability Anti patterns - Alex Mackey = 51:37
kEdlc_J4s8A = 6 years ago = Lightweight C# with Omnisharp and C# scripting - Filip W = 55:59
gZWdeMAXUlk = 6 years ago = JavaScript through History  - Cristian Prieto = 51:56
2fCfUUe8qok = 6 years ago = A Security Tester's Toolbox - Niall Merrigan = 59:51
WnnlPkip49g = 6 years ago = Scaling Professional Scrum with Visual Studio Team Services - Martin Hinshelwood = 49:22
QQwRg60VpIc = 6 years ago = .NET to The Power of R(1) - TJ Gokcen = 1:01:05
lwMzO8kxQ18 = 6 years ago = Diving into Elasticsearch with  .NET  - Russ Cam = 1:04:06
qRp_pJMCXKc = 6 years ago = Facebook Development with ASP.NET and Microsoft Azure -  Nick Pinheiro = 57:09
leCUq4Q3COk = 6 years ago = A developers guide to the UX galaxy  - Tess Ferrandez = 1:01:44
TqH9vh3gF8s = 6 years ago = Learning to program or speak a foreign language? - Anita Mongia = 45:56
wbEjhvlDZIM = 6 years ago = Developing Distributed Systems with Apache Mesos - ​Yaniv Rodenski = 1:00:08
BCdeMV0FXrU = 6 years ago = Look Ma! No servers! - Erwin van der Koogh = 52:57
04CbNB36HyA = 6 years ago = Power BI for the Developer - Peter Myers = 1:02:52
gaGF1imyfDg = 6 years ago = Let's talk Auth - Jordan Knight = 57:59
-cU27p4G9So = 6 years ago = Streams, lakes and oceans – working with on big data with Azure ML - Barbara Fusinska = 1:00:42
JMUSYugBn14 = 6 years ago = What's new in Xamarin.Forms - Michael Ridland = 1:00:52
X6a9bjNutEw = 6 years ago = Modern Authentication - Rob Moore = 1:02:13
wuPSYRi7Pt8 = 6 years ago = TypeScript : More than just another JS transpiler - Basarat Ali Syed = 57:27
_XaRjjHtEMI = 6 years ago = NDC Speaker Quotes: Troy Hunt = 0:26
iAzVFB7ta78 = 6 years ago = NDC Speaker Quotes: Woody Zuill = 0:23
9aOx7zuiBUo = 6 years ago = A picture is worth 1000 lines of code - Mike Minutillo = 55:43
krEhLbAOalE = 6 years ago = HTTP/2 : What you need to know - Robert Boedigheimer = 59:34
EtJtz9igY3k = 6 years ago = Create the Internet of Your Things - The Microsoft Azure IoT Suite - Stefano Tempesta = 1:01:04
Au52lvTPTTw = 6 years ago = Inside the new team build - Richard Banks = 56:36
BcuRv4PHxp0 = 6 years ago = Faster & less risky releases with feature flags - Edith Harbaugh = 59:04
qPBMY6eI_W8 = 6 years ago = Sherlock Homepage - A detective story about running large web services - Maarten Balliauw = 1:08:42
G75U442C7Us = 6 years ago = NDC London 2017: Dan North - NDC Indulgence = 0:35
pls1Vk_bw_Y = 6 years ago = Microtesting - Matt Davies and Rob Moore = 1:04:51
oTDjyMTZU1s = 6 years ago = A Walk Through Electron's Internals -  Brendan Forster = 53:14
p_4vA3mt8VE = 6 years ago = The Future of automated testing  - Gojko Adzic = 58:30
HjrJ2BoBktw = 6 years ago = Agile Project Management Anti-Patterns - Kasia Mrowca = 1:00:12
4KEqHD95Qwo = 6 years ago = Creative Technology in the Classroom: Lessons from Teachers and Students - Cathy Hunt = 1:01:36
YDB8nOs5iu8 = 6 years ago = ...because quality starts in your head - Sabine Wojcieszak = 47:50
i2P-KGUUxcg = 6 years ago = Angular 2 War StoriesAngular 2 War Stories - Adam Stephensen and Duncan Hunter = 1:02:25
I8WZYveGY-w = 6 years ago = Azure Machine Learning for the Developer - Peter Myers = 1:04:45
V69C7HDTB3o = 6 years ago = Functional Programming for the Everyman - Daniel Chambers = 1:02:16
i-8tTI-TRQk = 6 years ago = Continuous Delivery and DevOps and Robots; Oh my!   Fabien Ruffin and Jason Brown = 1:06:04
ckvwdZkwz48 = 6 years ago = Code it like C#, run it like Erlang - Philip Laureano = 54:32
qCmEs2FPIKg = 6 years ago = Domain Architecture Isomorphism and the Inverse Conway Maneuver - Dylan Beattie = 57:28
Xz-B0_oTTp8 = 6 years ago = Beyond Docker Buzzwords - Kiruthika Samapathy = 58:52
XFIDp4ueNLQ = 6 years ago = Debugging your communication for more success and efficiency in DevOps - Sabine Wojcieszak = 57:59
b0GUcL5JMOo = 6 years ago = Debugging Your Website with Fiddler and Chrome Developer Tools - Robert Boedigheimer = 1:01:19
3YJ1sB-z5-I = 6 years ago = Stairway to Cloud: Orleans Framework for building Halo-scale systems - Sergey Bykov = 1:09:54
nizO-YMIvX8 = 6 years ago = Project Kudu, The Magic Behind Azure App Services' Continuous Deployment - Emad Alashi = 46:04
qiK3vQkXn6U = 6 years ago = Soft Skills for the Developer - Mahesh Krishnan = 55:55
0hY_DrjY3-E = 6 years ago = This is not the Async you are looking for - Liam Westley = 1:03:06
Igr2FUrFcZg = 6 years ago = Real-time Twitter analysis with Reactive Extensions - Niall Connaughton = 1:01:58
lYgZZuwfRR8 = 6 years ago = Cloud Devops - Paul Stack and Lynn Langit = 1:03:24
dxwkYp4Fg3g = 6 years ago = Orleans Architecture Patterns - Sergey Bykov and John Azariah = 1:04:24
PSSTRHcwjs4 = 6 years ago = What makes React different? - Jake Ginnivan = 1:03:32
ikOiEVBq2E8 = 6 years ago = Teaching Kids Programming - Lynn Langit = 1:09:08
Vx5jcS89q7k = 6 years ago = The State of Mobile Development with JavaScript - John Bristowe = 1:03:40
hxApBX6Hoig = 6 years ago = Experience NDC London - A Software Developers Conference = 1:27
t7RAhyzupq8 = 6 years ago = The Agenda is out - NDC London 2017 = 0:46
kHVVdBqc5N8 = 6 years ago = Don’t Be Dilbert: Survival Tactics for Uninspiring Workplaces - Kylie Hunt = 56:58
x266Vy4tfT0 = 6 years ago = Cross Platform Mobile with XAML and MVVM - Nigel Sampson = 56:34
iTQWmXTfsEo = 6 years ago = Angular 2 for Angular 1 developers - Mohamed Meligy = 1:11:28
yEu6UkUcG90 = 6 years ago = Lessons learnt using Go - Paul Bouwer = 45:59
qEKNoz3hSsY = 6 years ago = Distributed Computing made easy with Azure Service Fabric - Magnus Mårtensson = 1:00:51
kz3YI2YGODs = 6 years ago = Pacts to the Rescue! Making your microservices play nicely together - Beth Skurrie = 39:04
4Mg98J7VdMs = 6 years ago = Azure IoT Service  - Dave Glover = 41:21
WpFXAkqPqKc = 6 years ago = Don't miss out on the Early Bird tickets for NDC London 2017 = 0:31
fZUt3FzGtKQ = 6 years ago = Windows 10 for IoT -  Dave Glover = 59:06
kS23n24GhD4 = 6 years ago = Visual Studio 2016 + Talk DevOps please - Adam Cogan = 51:23
Dw96iCXM9I8 = 6 years ago = Beyond console.log - Aaron Powell = 53:25
E86EH7pi2BI = 6 years ago = Call for papers deadline 1 October - NDC London 2017 = 0:30
OIhC0AbKLsw = 6 years ago = Docker and ServiceFabric - A taste of two platforms - Michele Bustamante = 1:10:04
wLG3V2jfaPk = 6 years ago = Centralised Logging    without the blood, sweat and tears   Paul Stack = 1:01:36
jPRnFfYtAzg = 6 years ago = Aurelia - Next Generation Web Apps - Ashley M Grant = 52:37
9Khvf1oExds = 6 years ago = The Experimentation Mindset - Doc Norton = 1:00:06
CS-Gg3iaeUo = 6 years ago = Rider Tips & Tricks - Hadi Hariri = 1:00:46
EJ86JSFQVOE = 6 years ago = Practical Microservice Security -  Laura Bell = 1:02:05
I-biS7E_ZVI = 6 years ago = How to Hack Your Own Mobile App -  Alec Tucker = 49:11
dmOfivnDav4 = 6 years ago = Holographic Programming – Exploring the HoloLens - Lars Klint = 1:01:13
jQGQQZlm90Q = 6 years ago = How to build  .NET Microservices - Richard Banks = 1:03:02
4YO4XmtPFQw = 6 years ago = F# in the Real World - Yan Cui = 1:00:00
_Iq4FWMGYyg = 6 years ago = Managing Enterprise and Consumer Identity with Azure Active Directory - Nick Pinheiro = 50:15
lCT5uGOkxOI = 6 years ago = Building Reactive Services using Functional Programming - Rachel Reese = 47:52
AaD0BQL7j30 = 6 years ago = Video Transcoding at Scale for ABC iview - Daphne Chong = 1:00:05
peKQWLWD5Xo = 6 years ago = Electron - Writing desktop applications using web technologies - Mahesh Krishnan & Cristian Prieto = 1:01:14
uSIPojyhs4E = 6 years ago = Creating Cross Platform Games with Unity - Brian Lagunas = 1:01:53
ZHms4njwF2M = 6 years ago = Web Diagnostics with a Glimpse into ASP.NET  - Anthony van der Hoorn = 1:04:11
agMWmsE-xHg = 6 years ago = Serverless - Sam Kroonenburg & Peter Sbarski = 58:21
LwcEQfjpa7w = 6 years ago = ASP.NET Core – OWIN in disguise - Chris Klug = 57:53
sH2mUncl2WU = 6 years ago = JavaScript's Most Wanted - Todd Gardner = 1:03:45
mhNIXMV3-ZI = 6 years ago = Awesome Node.js microservices in the cloud for (almost) free - Gojko Adzic = 1:06:05
t0frXaC9I7c = 6 years ago = DIY Security for the Amateur Superhero - Laura Bell = 58:04
qamzvLfX-Zo = 6 years ago = The Silver Bullet Syndrome - Hadi Hariri = 44:43
uEq-rivegew = 6 years ago = Open Source From The Trenches - James Newton-King = 53:12
zJ-MmYcOm4g = 6 years ago = Deploying and Scaling Microservices - Sam Newman = 1:04:15
SfWCRl75Kas = 6 years ago = The Technical Debt Trap - Doc Norton = 53:14
pyudECD-AfQ = 6 years ago = Patterns and practices for real-world event-driven microservices - Rachel Reese = 55:28
ghnY4S8unMM = 6 years ago = Building Code Analyzers with the new C# compiler platform (Roslyn) - Filip W = 1:00:51
eJYhBFh41Uo = 6 years ago = Effective Data Visualization  - David Giard = 50:42
eIOxJ2C6Fmk = 6 years ago = Deploying Docker Containers on Windows Server 2016 - Ben Hall = 57:50
r7tfrpvg-JU = 6 years ago = The Force Awakens: Mastering Your Inner Developer - Lars Klint = 52:02
XLKpCgB_XnA = 6 years ago = Microsoft Azure Without Microsoft - David Giard = 57:45
qdvNzm3upFw = 6 years ago = Where did you find that? - Niall Merrigan = 54:19
BR98recrBks = 6 years ago = Deploying Kubernetes, a Container Cluster Manager - Ben Hall = 1:00:42
F7cpp4bTTJg = 6 years ago = Continuous deployment in under 60 minutes with Octopus Deploy -  Damian Brady = 1:01:50
g8E1B7rTZBI = 6 years ago = The Rest of ReST - Dylan Beattie = 1:03:55
eyYtQLv8lss = 6 years ago = Faster Websites with WebPageTest - Nik Molnar = 58:50
LBUcDEzKxBo = 6 years ago = Performance as a First Class Feature with NBench - Aaron Stannard = 53:52
ozelpjr9SXE = 6 years ago = Akka.NET: The Future of Distributed Programming in .NET - Aaron Stannard = 1:13:35
3-Dy1GmiSoE = 6 years ago = 50 Shades of AppSec - Troy Hunt = 59:07
8d6kJYqFWoQ = 6 years ago = Node.js Crash Course for .NET Developers - David Neal = 59:40
rLNKaLwSmLY = 6 years ago = Looking forward to Bootstrap 4 - Shawn Wildermuth = 1:01:39
H2KkiRbDZyc = 6 years ago = Head to Head: Scott Allen and Jon Skeet  -  Scott Hanselman = 1:05:12
Ux5wUSOsEfc = 6 years ago = One kata, three languages -  Mark Seemann = 58:32
WGNDIXzKnV8 = 6 years ago = Accessing the Google Cloud Platform with C#  - Jon Skeet = 1:04:27
7Nj9ZjwOdFQ = 6 years ago = Life As A Developer: My Code Does Not Work Because I Am A Victim Of Complex Societal Factors... = 32:13
tPIQoV1YS8g = 6 years ago = What does an Open Source Microsoft Web Framework Look Like - Scott Hanselman = 1:05:26
Io0RYJLB674 = 6 years ago = A taste of EcmaScript 6: the language and the tools - Rob Richardson = 52:18
o3kjYL-C-Cw = 6 years ago = I say A “front end build pipeline” – You say WAT!? - Chris Klug = 1:01:32
JJJaS_adkFA = 6 years ago = How Real is this Cross Platform  .NET Thing Really? - Jon Galloway = 44:25
US8QG9I1XW0 = 6 years ago = Functional architecture - The pits of success - Mark Seemann = 1:00:10
T5ZnqtXqJmA = 6 years ago = Architecture in the Azure Cloud - Scott Hanselman = 57:28
-I3ntYVupGA = 6 years ago = Making Hacking Childs Play - Troy Hunt = 59:05
lJ-xjETzMAo = 6 years ago = The New Dragons in JavaScript - Scott Allen = 53:59
I3ou92_vV6g = 6 years ago = Solid ASP.NET Core -  Jimmy Bogard = 1:01:35
C6MPSLgsGGs = 6 years ago = ASP.NET Core for Angular, React, Knockout etc  developers - Steve Sanderson = 58:41
gtOoQqquZuw = 6 years ago = Building ASP.NET Core Kestrel - Damian Edwards & Jon Galloway = 59:54
NSjYQmu1u_k = 6 years ago = ASP.NET Core Deep(er) Dive - Damian Edwards = 1:01:24
Ko1zzs9K9dk = 6 years ago = What happens when...? - Tatham Oddie = 58:10
ND_1uAoGv-o = 6 years ago = NDC Sydney 2017 = 2:14
n0-b-5AOLHw = 6 years ago = NDC Conferences = 3:46
U6CeaA-Phqo = 6 years ago = Domain Driven Design: The Good Parts - Jimmy Bogard = 58:39
YI34UIMgkxs = 6 years ago = Keynote NDC Sydney 2016: If I knew then what I know now  - Scott Hanselman = 57:35
kej3YJDMAW4 = 6 years ago = ASP.NET Core Kestrel: Adventures in building a fast web server - Damian Edwards & David Fowler = 1:03:00
-iDpJ62_iKw = 6 years ago = Best Practices for using JS in your mobile app - Ricardo Minguez Pablos = 1:02:19
_-3lRihSXI4 = 6 years ago = HTTP 2.0 from the Developer's Viewpoint - Dave Methvin = 47:23
LiI1Gmm4BJw = 6 years ago = Open data in intelligent transport systems - Trond Smaavik & Jørgen Abrahamsen = 1:00:04
WuDy3rgGG2Q = 6 years ago = Performance Optimizations in the Wild - Oren Eini = 1:00:22
fd1_Miy1Clg = 6 years ago = There's Treasure Everywhere - Andrei Alexandrescu = 1:08:50
CHZW2O9Rmiw = 6 years ago = Functional web applications using F# and suave - Thomas Jansson = 55:03
bPUhuRwKQQk = 6 years ago = Continuous Integration and Delivery - from the trenches at www.lego.com -  Kristian Bank Erbou = 59:46
LjilQkxUW8g = 6 years ago = Working Distributed - How Does It Even Work? -  Brendan Forster = 54:43
Cjxl8yW63xo = 6 years ago = Bluetooth && Azure IoT hub == IoT - Or how to rule bilions of devices -  Jimmy Engström = 36:36
a4xn-7sUDkE = 6 years ago = .NET without Windows - Matt Ellis = 54:54
2VcbH_b174E = 6 years ago = Stairway to Cloud: Orleans Framework for building Halo-scale systems - Sergey Bykov = 1:06:55
79qPaR2EZyc = 6 years ago = Sensitive data in the cloud? You can’t do that! - Rune Grimstad = 51:27
lrziylOWBT4 = 6 years ago = Introduction to C++ Template Metaprogramming - Sasha Goldshtein = 56:32
RDalzi7mhdY = 6 years ago = Understanding parser combinators: a deep dive - Scott Wlaschin = 53:06
DE8deJnZ4P8 = 6 years ago = Modern Data Applications with Entity Framework 7 - Ido Flatow = 1:09:55
ZgnkilrR-F8 = 6 years ago = How to do a really good product demo - Katrin Grothues = 48:28
4w9twvw0MFg = 6 years ago = Performance is not an Option- Building services with GRPC and Cassandra - Dave Bechberger = 1:00:21
ozOgzlxIsdg = 6 years ago = Generic Locking in C++ -  Andrei Alexandrescu = 1:01:13
1xU-983EwfU = 6 years ago = MicroMonolith - Top anti-patterns of distributed systems - Michal Franc = 43:11
qF6R7R-Un1Q = 6 years ago = Automated UI Testing for iOS and Android Mobile Apps - Karl Krukow = 58:31
thSlnISxiQw = 6 years ago = .NET Data Security : Hope is not a Strategy - Stephen Haunts = 51:54
yBy8JvKZHh8 = 6 years ago = Is your code ready for .NET Core? - Mark Rendle = 1:01:58
zZIyEn4jF2U = 6 years ago = A Piece of Cake - C# powered cross platform build automation - Gary Ewan Park = 54:48
0gaeM1oqQGs = 6 years ago = Hacking in 2016 - How is our systems broken? - Chris Dale = 57:53
f3Gs-EMIu6U = 6 years ago = IoT at home - The solution to all your spare time problems - Karl-Henrik Nilsson = 45:32
u2uygV2CkeM = 6 years ago = Cloud Patterns - Tamir Dresher = 34:50
K_AlkvZsUus = 6 years ago = The F#orce Awakens - Evelina Gabasova = 48:51
L_DR9L12jNI = 6 years ago = Real World HoloLens Mixed Reality Development with Unity - Be Part of the Future - Rene Schulte = 1:00:21
ocRQwN2jmZU = 6 years ago = Optimizing the Programmer: Get More Done Faster - Dave Rael = 58:29
talX76v7JB4 = 6 years ago = Windows IoT Core or Corny - Karl-Henrik Nilsson = 38:39
mBuZ2O1pRws = 6 years ago = ASP.NET Core 1: What has changed for MVC and Web API developers? - Manfred Steyer = 1:02:52
ce_2AWH7UJU = 6 years ago = Safety: off --- How not to shoot yourself in the foot with C++ atomics - Anthony Williams = 1:03:13
T4sD6tjrF8Q = 6 years ago = Scaling large Angular apps - Jad Joubran = 53:23
i9tkLLQOThw = 6 years ago = Keynote: Yesterday’s Technology is Dead, Today’s is on Life Support - Troy Hunt = 51:31
wbIMJNmBFpE = 6 years ago = REPL Driven Development, Scrum, and the Wright Brothers - Jamie Dixon = 53:26
MzX0OnNl-AE = 6 years ago = Head to Head #2: K. Scott Allen and Jimmy Bogard = 57:40
E6_UyQPmiSg = 6 years ago = A High-Performance Solution to Microservices UI Composition - Arif Wider & Alexey Gravanov = 1:06:11
q8wueg2hswA = 7 years ago = What every Node.js developer needs to know about Elixir - Bryan Hunter = 1:05:40
S1M3riYHdEU = 7 years ago = Talk To Your Microservice Via a Chat Bot, not UI  - Yegor Bugayenko = 43:37
4DZCx_Uky-Y = 7 years ago = Becoming a Social Developer -  Jeremy Clark = 59:42
a6W4WewAQBs = 7 years ago = Bringing beacons to the Windows platform - Michał Łusiak = 46:59
6I_GwgoGm1w = 7 years ago = Choosing a JavaScript Framework - Rob Eisenberg = 1:01:33
FiBDwiWy4jk = 7 years ago = NDC Oslo 2016: sequential, concurrent and parallel programming = 0:50
Og97z2Kyi0A = 7 years ago = NDC Oslo 2016: Pre-Conference Workshops highlights = 1:00
gq2TvpF63_c = 7 years ago = NDC Oslo 2016: How to be a social developer = 0:59
s9YmkpvRows = 7 years ago = NDC Oslo 2016: Highlights from day 2 = 0:28
"""

"""
>>> videos = scrapetube.get_channel("UCTdw38Cw6jcm0atBPA39a0Q")
>>> for video in videos:
...     for key, value in video.items():
...             print(f"{key}: {value}")
...
videoId: 1DuxTlvmaNM
thumbnail: {'thumbnails': [{'url': 'https://i.ytimg.com/vi/1DuxTlvmaNM/hqdefault.jpg?sqp=-oaymwEbCKgBEF5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLDFygXFvyqgCo3zDNEkjqejIaVRhA', 'width': 168, 'height': 94}, {'url': 'https://i.ytimg.com/vi/1DuxTlvmaNM/hqdefault.jpg?sqp=-oaymwEbCMQBEG5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLCK6T9WZDQY9Zi1XE9umML2TkXXuw', 'width': 196, 'height': 110}, {'url': 'https://i.ytimg.com/vi/1DuxTlvmaNM/hqdefault.jpg?sqp=-oaymwEcCPYBEIoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLABQ_abyMnk0SM2K_4AyEwQ57zPyg', 'width': 246, 'height': 138}, {'url': 'https://i.ytimg.com/vi/1DuxTlvmaNM/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCBR0RZumYJa6w6Lb_fL_DLiTcBOg', 'width': 336, 'height': 188}]}
title: {'runs': [{'text': 'Managing Kubernetes the GitOps way with Flux - Jeff French - NDC Oslo 2023'}], 'accessibility': {'accessibilityData': {'label': 'Managing Kubernetes the GitOps way with Flux - Jeff French - NDC Oslo 2023 by NDC Conferences 4 days ago 1 hour 1,003 views'}}}
descriptionSnippet: {'runs': [{'text': 'In this session, we will explore the benefits and best practices of using the Flux GitOps framework for managing Kubernetes clusters. We will start with a brief overview of GitOps and the Flux...'}]}
publishedTimeText: {'simpleText': '4 days ago'}
lengthText: {'accessibility': {'accessibilityData': {'label': '1 hour, 38 seconds'}}, 'simpleText': '1:00:38'}
viewCountText: {'simpleText': '1,003 views'}
navigationEndpoint: {'clickTrackingParams': 'CO0BENwwIhMIp_vlyoyZgAMVbswRCB3VdQcZWhhVQ1RkdzM4Q3c2amNtMGF0QlBBMzlhMFGaAQYQ8jgY4Ac=', 'commandMetadata': {'webCommandMetadata': {'url': '/watch?v=1DuxTlvmaNM', 'webPageType': 'WEB_PAGE_TYPE_WATCH', 'rootVe': 3832}}, 'watchEndpoint': {'videoId': '1DuxTlvmaNM', 'watchEndpointSupportedOnesieConfig': {'html5PlaybackOnesieConfig': {'commonConfig': {'url': 'https://rr3---sn-1gi7znes.googlevideo.com/initplayback?source=youtube&oeis=1&c=WEB&oad=3200&ovd=3200&oaad=11000&oavd=11000&ocs=700&oewis=1&oputc=1&ofpcc=1&msp=1&odepv=1&id=d43bb14e5be668d3&ip=213.142.178.228&initcwndbps=1770000&mt=1689624085&oweuc=&pxtags=Cg4KAnR4Egg0NTE3MDA1OA&rxtags=Cg4KAnR4Egg0NTE3MDA1OA%2CCg4KAnR4Egg0NTE3MDA1OQ'}}}}}
trackingParams: CO0BENwwIhMIp_vlyoyZgAMVbswRCB3VdQcZQNPRmd_lqeyd1AE=
showActionMenu: False
shortViewCountText: {'accessibility': {'accessibilityData': {'label': '1K views'}}, 'simpleText': '1K views'}
menu: {'menuRenderer': {'items': [{'menuServiceItemRenderer': {'text': {'runs': [{'text': 'Add to queue'}]}, 'icon': {'iconType': 'ADD_TO_QUEUE_TAIL'}, 'serviceEndpoint': {'clickTrackingParams': 'CPIBEP6YBBgFIhMIp_vlyoyZgAMVbswRCB3VdQcZ', 'commandMetadata': {'webCommandMetadata': {'sendPost': True}}, 'signalServiceEndpoint': {'signal': 'CLIENT_SIGNAL', 'actions': [{'clickTrackingParams': 'CPIBEP6YBBgFIhMIp_vlyoyZgAMVbswRCB3VdQcZ', 'addToPlaylistCommand': {'openMiniplayer': True, 'videoId': '1DuxTlvmaNM', 'listType': 'PLAYLIST_EDIT_LIST_TYPE_QUEUE', 'onCreateListCommand': {'clickTrackingParams': 'CPIBEP6YBBgFIhMIp_vlyoyZgAMVbswRCB3VdQcZ', 'commandMetadata': {'webCommandMetadata': {'sendPost': True, 'apiUrl': '/youtubei/v1/playlist/create'}}, 'createPlaylistServiceEndpoint': {'videoIds': ['1DuxTlvmaNM'], 'params': 'CAQ%3D'}}, 'videoIds': ['1DuxTlvmaNM']}}]}}, 'trackingParams': 'CPIBEP6YBBgFIhMIp_vlyoyZgAMVbswRCB3VdQcZ'}}, {'menuServiceItemDownloadRenderer': {'serviceEndpoint': {'clickTrackingParams': 'CPEBENGqBRgGIhMIp_vlyoyZgAMVbswRCB3VdQcZ', 'offlineVideoEndpoint': {'videoId': '1DuxTlvmaNM', 'onAddCommand': {'clickTrackingParams': 'CPEBENGqBRgGIhMIp_vlyoyZgAMVbswRCB3VdQcZ', 'getDownloadActionCommand': {'videoId': '1DuxTlvmaNM', 'params': 'CAI%3D'}}}}, 'trackingParams': 'CPEBENGqBRgGIhMIp_vlyoyZgAMVbswRCB3VdQcZ'}}, {'menuServiceItemRenderer': {'text': {'runs': [{'text': 'Share'}]}, 'icon': {'iconType': 'SHARE'}, 'serviceEndpoint': {'clickTrackingParams': 'CO0BENwwIhMIp_vlyoyZgAMVbswRCB3VdQcZ', 'commandMetadata': {'webCommandMetadata': {'sendPost': True, 'apiUrl': '/youtubei/v1/share/get_share_panel'}}, 'shareEntityServiceEndpoint': {'serializedShareEntity': 'CgsxRHV4VGx2bWFOTQ%3D%3D', 'commands': [{'clickTrackingParams': 'CO0BENwwIhMIp_vlyoyZgAMVbswRCB3VdQcZ', 'openPopupAction': {'popup': {'unifiedSharePanelRenderer': {'trackingParams': 'CPABEI5iIhMIp_vlyoyZgAMVbswRCB3VdQcZ', 'showLoadingSpinner': True}}, 'popupType': 'DIALOG', 'beReused': True}}]}}, 'trackingParams': 'CO0BENwwIhMIp_vlyoyZgAMVbswRCB3VdQcZ'}}], 'trackingParams': 'CO0BENwwIhMIp_vlyoyZgAMVbswRCB3VdQcZ', 'accessibility': {'accessibilityData': {'label': 'Action menu'}}}}
thumbnailOverlays: [{'thumbnailOverlayTimeStatusRenderer': {'text': {'accessibility': {'accessibilityData': {'label': '1 hour, 38 seconds'}}, 'simpleText': '1:00:38'}, 'style': 'DEFAULT'}}, {'thumbnailOverlayToggleButtonRenderer': {'isToggled': False, 'untoggledIcon': {'iconType': 'WATCH_LATER'}, 'toggledIcon': {'iconType': 'CHECK'}, 'untoggledTooltip': 'Watch later', 'toggledTooltip': 'Added', 'untoggledServiceEndpoint': {'clickTrackingParams': 'CO8BEPnnAxgBIhMIp_vlyoyZgAMVbswRCB3VdQcZ', 'commandMetadata': {'webCommandMetadata': {'sendPost': True, 'apiUrl': '/youtubei/v1/browse/edit_playlist'}}, 'playlistEditEndpoint': {'playlistId': 'WL', 'actions': [{'addedVideoId': '1DuxTlvmaNM', 'action': 'ACTION_ADD_VIDEO'}]}}, 'toggledServiceEndpoint': {'clickTrackingParams': 'CO8BEPnnAxgBIhMIp_vlyoyZgAMVbswRCB3VdQcZ', 'commandMetadata': {'webCommandMetadata': {'sendPost': True, 'apiUrl': '/youtubei/v1/browse/edit_playlist'}}, 'playlistEditEndpoint': {'playlistId': 'WL', 'actions': [{'action': 'ACTION_REMOVE_VIDEO_BY_VIDEO_ID', 'removedVideoId': '1DuxTlvmaNM'}]}}, 'untoggledAccessibility': {'accessibilityData': {'label': 'Watch later'}}, 'toggledAccessibility': {'accessibilityData': {'label': 'Added'}}, 'trackingParams': 'CO8BEPnnAxgBIhMIp_vlyoyZgAMVbswRCB3VdQcZ'}}, {'thumbnailOverlayToggleButtonRenderer': {'untoggledIcon': {'iconType': 'ADD_TO_QUEUE_TAIL'}, 'toggledIcon': {'iconType': 'PLAYLIST_ADD_CHECK'}, 'untoggledTooltip': 'Add to queue', 'toggledTooltip': 'Added', 'untoggledServiceEndpoint': {'clickTrackingParams': 'CO4BEMfsBBgCIhMIp_vlyoyZgAMVbswRCB3VdQcZ', 'commandMetadata': {'webCommandMetadata': {'sendPost': True}}, 'signalServiceEndpoint': {'signal': 'CLIENT_SIGNAL', 'actions': [{'clickTrackingParams': 'CO4BEMfsBBgCIhMIp_vlyoyZgAMVbswRCB3VdQcZ', 'addToPlaylistCommand': {'openMiniplayer': True, 'videoId': '1DuxTlvmaNM', 'listType': 'PLAYLIST_EDIT_LIST_TYPE_QUEUE', 'onCreateListCommand': {'clickTrackingParams': 'CO4BEMfsBBgCIhMIp_vlyoyZgAMVbswRCB3VdQcZ', 'commandMetadata': {'webCommandMetadata': {'sendPost': True, 'apiUrl': '/youtubei/v1/playlist/create'}}, 'createPlaylistServiceEndpoint': {'videoIds': ['1DuxTlvmaNM'], 'params': 'CAQ%3D'}}, 'videoIds': ['1DuxTlvmaNM']}}]}}, 'untoggledAccessibility': {'accessibilityData': {'label': 'Add to queue'}}, 'toggledAccessibility': {'accessibilityData': {'label': 'Added'}}, 'trackingParams': 'CO4BEMfsBBgCIhMIp_vlyoyZgAMVbswRCB3VdQcZ'}}, {'thumbnailOverlayNowPlayingRenderer': {'text': {'runs': [{'text': 'Now playing'}]}}}]
videoId: AYU0vw6IyUY


thumbnail: {'thumbnails': [{'url': 'https://i.ytimg.com/vi/AYU0vw6IyUY/hqdefault.jpg?sqp=-oaymwEbCKgBEF5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLCU_3rIVvaQzXp6F0Ef7fcvIZx5xw', 'width': 168, 'height': 94}, {'url': 'https://i.ytimg.com/vi/AYU0vw6IyUY/hqdefault.jpg?sqp=-oaymwEbCMQBEG5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLA6Q-O5wWBod6W3PXE8JMS1484hcQ', 'width': 196, 'height': 110}, {'url': 'https://i.ytimg.com/vi/AYU0vw6IyUY/hqdefault.jpg?sqp=-oaymwEcCPYBEIoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCD08KENYaqx17vmC0K3W2ks2cdHQ', 'width': 246, 'height': 138}, {'url': 'https://i.ytimg.com/vi/AYU0vw6IyUY/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDMFCdIroiTRm6rjV9bg8Q3kEBcAA', 'width': 336, 'height': 188}]}
title: {'runs': [{'text': 'Make a great-looking 3D landscape visualization! - Kristoffer Dyrkorn - NDC Oslo 2023'}], 'accessibility': {'accessibilityData': {'label': 'Make a great-looking 3D landscape visualization! - Kristoffer Dyrkorn - NDC Oslo 2023 by NDC Conferences 4 days ago 59 minutes 1,065 views'}}}
descriptionSnippet: {'runs': [{'text': 'In this session you will learn all you need to create your own 3D landscape visualizations in the browser. I will go through:\n\n- where to get free, high quality, data\n- how to preprocess and...'}]}
publishedTimeText: {'simpleText': '4 days ago'}
lengthText: {'accessibility': {'accessibilityData': {'label': '59 minutes, 6 seconds'}}, 'simpleText': '59:06'}
viewCountText: {'simpleText': '1,065 views'}
navigationEndpoint: {'clickTrackingParams': 'COYBENwwIhMIp_vlyoyZgAMVbswRCB3VdQcZWhhVQ1RkdzM4Q3c2amNtMGF0QlBBMzlhMFGaAQYQ8jgY4Ac=', 'commandMetadata': {'webCommandMetadata': {'url': '/watch?v=AYU0vw6IyUY', 'webPageType': 'WEB_PAGE_TYPE_WATCH', 'rootVe': 3832}}, 'watchEndpoint': {'videoId': 'AYU0vw6IyUY', 'watchEndpointSupportedOnesieConfig': {'html5PlaybackOnesieConfig': {'commonConfig': {'url': 'https://rr1---sn-1gi7znek.googlevideo.com/initplayback?source=youtube&oeis=1&c=WEB&oad=3200&ovd=3200&oaad=11000&oavd=11000&ocs=700&oewis=1&oputc=1&ofpcc=1&msp=1&odepv=1&id=018534bf0e88c946&ip=213.142.178.228&initcwndbps=1770000&mt=1689624085&oweuc=&pxtags=Cg4KAnR4Egg0NTE3MDA1OA&rxtags=Cg4KAnR4Egg0NTE3MDA1OA%2CCg4KAnR4Egg0NTE3MDA1OQ'}}}}}
trackingParams: COYBENwwIhMIp_vlyoyZgAMVbswRCB3VdQcZQMaSo_Twl83CAQ==
showActionMenu: False
shortViewCountText: {'accessibility': {'accessibilityData': {'label': '1K views'}}, 'simpleText': '1K views'}
menu: {'menuRenderer': {'items': [{'menuServiceItemRenderer': {'text': {'runs': [{'text': 'Add to queue'}]}, 'icon': {'iconType': 'ADD_TO_QUEUE_TAIL'}, 'serviceEndpoint': {'clickTrackingParams': 'COsBEP6YBBgFIhMIp_vlyoyZgAMVbswRCB3VdQcZ', 'commandMetadata': {'webCommandMetadata': {'sendPost': True}}, 'signalServiceEndpoint': {'signal': 'CLIENT_SIGNAL', 'actions': [{'clickTrackingParams': 'COsBEP6YBBgFIhMIp_vlyoyZgAMVbswRCB3VdQcZ', 'addToPlaylistCommand': {'openMiniplayer': True, 'videoId': 'AYU0vw6IyUY', 'listType': 'PLAYLIST_EDIT_LIST_TYPE_QUEUE', 'onCreateListCommand': {'clickTrackingParams': 'COsBEP6YBBgFIhMIp_vlyoyZgAMVbswRCB3VdQcZ', 'commandMetadata': {'webCommandMetadata': {'sendPost': True, 'apiUrl': '/youtubei/v1/playlist/create'}}, 'createPlaylistServiceEndpoint': {'videoIds': ['AYU0vw6IyUY'], 'params': 'CAQ%3D'}}, 'videoIds': ['AYU0vw6IyUY']}}]}}, 'trackingParams': 'COsBEP6YBBgFIhMIp_vlyoyZgAMVbswRCB3VdQcZ'}}, {'menuServiceItemDownloadRenderer': {'serviceEndpoint': {'clickTrackingParams': 'COoBENGqBRgGIhMIp_vlyoyZgAMVbswRCB3VdQcZ', 'offlineVideoEndpoint': {'videoId': 'AYU0vw6IyUY', 'onAddCommand': {'clickTrackingParams': 'COoBENGqBRgGIhMIp_vlyoyZgAMVbswRCB3VdQcZ', 'getDownloadActionCommand': {'videoId': 'AYU0vw6IyUY', 'params': 'CAI%3D'}}}}, 'trackingParams': 'COoBENGqBRgGIhMIp_vlyoyZgAMVbswRCB3VdQcZ'}}, {'menuServiceItemRenderer': {'text': {'runs': [{'text': 'Share'}]}, 'icon': {'iconType': 'SHARE'}, 'serviceEndpoint': {'clickTrackingParams': 'COYBENwwIhMIp_vlyoyZgAMVbswRCB3VdQcZ', 'commandMetadata': {'webCommandMetadata': {'sendPost': True, 'apiUrl': '/youtubei/v1/share/get_share_panel'}}, 'shareEntityServiceEndpoint': {'serializedShareEntity': 'CgtBWVUwdnc2SXlVWQ%3D%3D', 'commands': [{'clickTrackingParams': 'COYBENwwIhMIp_vlyoyZgAMVbswRCB3VdQcZ', 'openPopupAction': {'popup': {'unifiedSharePanelRenderer': {'trackingParams': 'COkBEI5iIhMIp_vlyoyZgAMVbswRCB3VdQcZ', 'showLoadingSpinner': True}}, 'popupType': 'DIALOG', 'beReused': True}}]}}, 'trackingParams': 'COYBENwwIhMIp_vlyoyZgAMVbswRCB3VdQcZ'}}], 'trackingParams': 'COYBENwwIhMIp_vlyoyZgAMVbswRCB3VdQcZ', 'accessibility': {'accessibilityData': {'label': 'Action menu'}}}}
thumbnailOverlays: [{'thumbnailOverlayTimeStatusRenderer': {'text': {'accessibility': {'accessibilityData': {'label': '59 minutes, 6 seconds'}}, 'simpleText': '59:06'}, 'style': 'DEFAULT'}}, {'thumbnailOverlayToggleButtonRenderer': {'isToggled': False, 'untoggledIcon': {'iconType': 'WATCH_LATER'}, 'toggledIcon': {'iconType': 'CHECK'}, 'untoggledTooltip': 'Watch later', 'toggledTooltip': 'Added', 'untoggledServiceEndpoint': {'clickTrackingParams': 'COgBEPnnAxgBIhMIp_vlyoyZgAMVbswRCB3VdQcZ', 'commandMetadata': {'webCommandMetadata': {'sendPost': True, 'apiUrl': '/youtubei/v1/browse/edit_playlist'}}, 'playlistEditEndpoint': {'playlistId': 'WL', 'actions': [{'addedVideoId': 'AYU0vw6IyUY', 'action': 'ACTION_ADD_VIDEO'}]}}, 'toggledServiceEndpoint': {'clickTrackingParams': 'COgBEPnnAxgBIhMIp_vlyoyZgAMVbswRCB3VdQcZ', 'commandMetadata': {'webCommandMetadata': {'sendPost': True, 'apiUrl': '/youtubei/v1/browse/edit_playlist'}}, 'playlistEditEndpoint': {'playlistId': 'WL', 'actions': [{'action': 'ACTION_REMOVE_VIDEO_BY_VIDEO_ID', 'removedVideoId': 'AYU0vw6IyUY'}]}}, 'untoggledAccessibility': {'accessibilityData': {'label': 'Watch later'}}, 'toggledAccessibility': {'accessibilityData': {'label': 'Added'}}, 'trackingParams': 'COgBEPnnAxgBIhMIp_vlyoyZgAMVbswRCB3VdQcZ'}}, {'thumbnailOverlayToggleButtonRenderer': {'untoggledIcon': {'iconType': 'ADD_TO_QUEUE_TAIL'}, 'toggledIcon': {'iconType': 'PLAYLIST_ADD_CHECK'}, 'untoggledTooltip': 'Add to queue', 'toggledTooltip': 'Added', 'untoggledServiceEndpoint': {'clickTrackingParams': 'COcBEMfsBBgCIhMIp_vlyoyZgAMVbswRCB3VdQcZ', 'commandMetadata': {'webCommandMetadata': {'sendPost': True}}, 'signalServiceEndpoint': {'signal': 'CLIENT_SIGNAL', 'actions': [{'clickTrackingParams': 'COcBEMfsBBgCIhMIp_vlyoyZgAMVbswRCB3VdQcZ', 'addToPlaylistCommand': {'openMiniplayer': True, 'videoId': 'AYU0vw6IyUY', 'listType': 'PLAYLIST_EDIT_LIST_TYPE_QUEUE', 'onCreateListCommand': {'clickTrackingParams': 'COcBEMfsBBgCIhMIp_vlyoyZgAMVbswRCB3VdQcZ', 'commandMetadata': {'webCommandMetadata': {'sendPost': True, 'apiUrl': '/youtubei/v1/playlist/create'}}, 'createPlaylistServiceEndpoint': {'videoIds': ['AYU0vw6IyUY'], 'params': 'CAQ%3D'}}, 'videoIds': ['AYU0vw6IyUY']}}]}}, 'untoggledAccessibility': {'accessibilityData': {'label': 'Add to queue'}}, 'toggledAccessibility': {'accessibilityData': {'label': 'Added'}}, 'trackingParams': 'COcBEMfsBBgCIhMIp_vlyoyZgAMVbswRCB3VdQcZ'}}, {'thumbnailOverlayNowPlayingRenderer': {'text': {'runs': [{'text': 'Now playing'}]}}}]
"""