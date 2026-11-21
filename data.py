"""All site content lives here, so you can update the portfolio without touching the HTML templates."""

# Images are currently served from the original Odoo site.
# To host them yourself, put them in static/images/ and change IMG to "/static/images/".
IMG = "https://hala-ghareeb.odoo.com/web/image/"

EMAIL = "hala.ghareeb117@gmail.com"

# (endpoint name, menu label)
NAV = [
    ("home", "Home"),
    ("solutions", "Solutions"),
    ("dashboards", "Dashboards"),
    ("educational_projects", "Educational Projects"),
    ("training_and_skills", "Training and Skills"),
    ("achievements", "Achievements"),
]

SOCIAL = [
    {"name": "LinkedIn", "icon": "linkedin", "url": "https://www.linkedin.com/in/halaghareeb/"},
    {"name": "GitHub", "icon": "github", "url": "https://github.com/halaghareeb"},
    {"name": "YouTube", "icon": "youtube", "url": "https://www.youtube.com/@Hala_Ghareeb"},
    {"name": "Esri Community", "icon": "community",
     "url": "https://community.esri.com/t5/user/viewprofilepage/user-id/469987"},
]

# ------------------------------------------------------------------ HOME
PROFILE = {
    "name": "Hala Ghareeb",
    "role": "Geospatial Engineer",
    "photo": IMG + "828-37386edb/WhatsApp%20Image%202026-10-11%20at%2011.14.58%20AM.webp",
    "sub": "Turning complex data into clear insights by delivering robust solutions and Insights that create real-world impact.",
    "skills": ["GeoAI", "Machine learning", "Python", "Data analytics",
               "Smart Cities", "Sustainability and conservation"],
}

EDUCATION = [
    {
        "title": "MSc in Geospatial Technologies — Erasmus Mundus Joint Master",
        "date": "Sep 2024 – Feb 2026",
        "institutions": [
            "Institute for Geoinformatics (IFGI), University of Münster, Germany",
            "NOVA Information Management School (NOVA IMS), NOVA University Lisbon, Portugal",
            "Institute of New Imaging Technologies (INIT), Universitat Jaume I (UJI), Castellón, Spain",
        ],
        "highlights": [
            {"text": "Thesis: The Impact of Prior Survey Knowledge and Virtual Global Landmarks on "
                     "Spatial Knowledge Acquisition — Grade: 18/20",
             "link": "https://run.unl.pt/entities/publication/7cc1a52a-e9fb-4651-b205-ef014f048021"},
        ],
        "topics": ["GIScience", "Spatial Analysis and Statistics", "Machine Learning", "Remote Sensing",
                   "UAVs", "Image Processing", "Data Visualization", "Data Mining", "Spatial Cognition",
                   "Web Development"],
    },
    {
        "title": "9-Month Diploma Scholarship in Geoinformatics",
        "date": "Sep 2019 – Jun 2020",
        "institutions": ["Information Technology Institute (ITI), Egypt"],
        "highlights": [{"text": "Graduation project: A road-maintenance web application"}],
        "topics": ["GIS", "Computer Networks", "Programming & Scripting (C#, Python, .NET, MERN)",
                   "Client-Side Technologies", "Machine Learning (SAS)", "Remote Sensing",
                   "Database Management (SQL)"],
    },
    {
        "title": "BSc in Surveying and Geomatics Engineering",
        "date": "Sep 2014 – Jul 2019",
        "institutions": ["Faculty of Engineering at Shoubra, Benha University, Egypt"],
        "highlights": [
            {"text": "Graduation project: Developed a GIS-based framework to identify optimal routes "
                     "for potential road networks."},
            {"text": "Ranked fifth in my class"},
        ],
        "topics": ["GIS", "Geospatial Statistics", "Remote Sensing", "Surveying", "3D High-Precision Mapping",
                   "Map Projection", "Geodesy", "GPS", "Photogrammetry", "Road Design"],
    },
]

EXPERIENCE = [
    {
        "title": "GIS Instructor",
        "date": "Jan 2021 – Present",
        "Affiliations": ["Freelance, Remote"],
        "highlights": [
            {"text": "Delivering GIS training courses and technical instruction."},
            {"text": "Teaching Spatial Analysis, Geospatial Data Management, Python, and ArcPy."},
        ],
        "skills": ["Spatial Analysis", "Geospatial Data Management", "Python Programming", "ArcPy",
                   "GIS Training & Knowledge Transfer"],
    },
    {
        "title": "Solutions & Presales Engineer",
        "date": "Jun 2022 – Aug 2024",
        "Affiliations": ["Esri North Africa (Esri NA), New Cairo, Egypt"],
        "highlights": [
            {"text": "Translating business requirements to tailored solutions and applications."},
            {"text": "Developed solutions for environment, AEC, conservation and sustainability, education, agriculture, retail, "
                     "banking, manufacturing, distribution, and fleet management."},
            {"text": "Developed GIS geoportals, dashboards, and web applications to visualize data, maps and insights."},
            {"text": "Prepared technical proposals in response to client requirements and tenders."},
            {"text": "Delivered internship programs for engineering students."},
        ],
        "skills": ["GIS Solutions Design", "Technical Presales & Demonstrations", "Enterprise GIS",
                   "Web GIS & Dashboards", "Data Visualization", "Business Analysis",
                   "GIS Workflow Development", "Programming & Integration"],
    },
    {
        "title": "Platform Configuration Engineer",
        "date": "Jul 2020 – Jun 2022",
        "Affiliations": ["Esri North Africa (Esri NA), Egypt"],
        "highlights": [
            {"text": "Implemented and delivered end-to-end GIS projects, covering data management, spatial "
                     "analysis, and application development."},
            {"text": "Configured and deployed Esri applications to address specific project requirements."},
            {"text": "Developed scripts and customized workflows using Python, SQL, Esri Arcade, and front-end technologies."},
            {"text": "Delivered technical training on ArcGIS products, including Python Scripting for ArcGIS, "
                     "Geodatabase Management, Spatial analysis, and Essential Workflows."},
         
        ],
        "skills": ["Enterprise GIS Implementation", "GIS Application Development",
                   "Python & ArcPy", "SQL & Databases", "GIS Automation", "Esri Platform Configuration",
                   "Technical Training & Support"],
    },
]

EXPLORE = [
    {"endpoint": "solutions", "label": "Solutions", "icon": "layers"},
    {"endpoint": "dashboards", "label": "Dashboards", "icon": "dashboard"},
    {"endpoint": "educational_projects", "label": "Educational Projects",
     "icon": "graduation-cap"},
    {"endpoint": "training_and_skills", "label": "Latest Work", "icon": "briefcase"},
    {"endpoint": "achievements", "label": "Achievements", "icon": "trophy"},
]

# ------------------------------------------------------------------ SOLUTIONS
SOLUTIONS = [
    {"title": "Egypt Logistics Platform",
     "image": IMG + "559-97d57303/Screenshot%202026-01-05%20053449.png",
     "url": "https://experience.arcgis.com/experience/a1a17e1609de4a67b5955bd8d1be65c5/"},
    {"title": "Arab Climate Change Platform",
     "image": IMG + "555-44442603/Screenshot%202026-01-05%20061904.png",
     "url": "https://experience.arcgis.com/experience/df149f929b27432eab2141671cc3d226/page/"
            "%D8%A7%D9%84%D8%B1%D8%A6%D9%8A%D8%B3%D9%8A%D8%A9?locale=ar"},
    {"title": "Business Sector StoryMap",
     "image": IMG + "550-10e325c0/Screenshot%202026-01-05%20231642s.png",
     "url": "https://storymaps.arcgis.com/stories/b151006a1cf74878a9e255e8e3915e7a"},
    {"title": "Green Energy Resources Management",
     "image": IMG + "570-c799e605/Screenshot%202026-01-05%20062006.webp",
     "url": "https://experience.arcgis.com/experience/f47f37383a83460b81f14ebf10a0e639"},
    {"title": "Geographic Portal of the Ministry of Education in Tunisia",
     "image": IMG + "568-79157bc4/Screenshot%202026-01-05%20230831.webp",
     "url": "https://experience.arcgis.com/experience/73cd83ffacde46399f9321ffdc83317b"},
    {"title": "Mostaqbal Misr Dashboard",
     "image": IMG + "572-a5807525/Screenshot%202026-01-05%20232250.webp",
     "url": "https://esrina.maps.arcgis.com/apps/dashboards/16c2e7746785485486d3cfca05c32c37"},
    {"title": "Portal of the Libyan Post, Telecommunications and Information Technology Holding Company",
     "image": IMG + "574-14132493/Screenshot%202026-01-05%20175851.webp",
     "url": "https://experience.arcgis.com/experience/c1bc2078b53941aa95683cc9201c967f/"},
]

# ------------------------------------------------------------------ DASHBOARDS
DASHBOARDS = [
    {
        "title": "Workforce Performance Dashboard",
        "image": IMG + "643-d4173059/screenshot_4_26_2026_12-07-04%20AM.png",
        "url": "https://esrina.maps.arcgis.com/apps/dashboards/a6dda17bc6534efe9c91d5891f0644e5#locale=ar",
    },
    {
        "title": "Smart Agriculture Monitoring Dashboard",
        "image": IMG + "641-49d6fb63/screenshot_4_26_2026_12-05-24%20AM.png",
        "url": "https://esrina.maps.arcgis.com/apps/dashboards/16c2e7746785485486d3cfca05c32c37#",
    },
    {
        "title": "Tunisia Workforce Performance Dashboard",
        "image": IMG + "640-9b88f92d/screenshot_4_26_2026_12-04-22%20AM.png",
        "url": "https://esrieg.maps.arcgis.com/apps/dashboards/6191168c7bf1443e9f818641dfad5292#locale=ar",
    },
    {
        "title": "Retail Store Sales Performance Dashboard",
        "image": IMG + "657-7275d531/screenshot_4_26_2026_12-01-39%20AM.png",
        "url": "https://esrieg.maps.arcgis.com/apps/dashboards/5944e6ed85544af29299702b2a8c1d02#",
    },
    {
        "title": "GID Water Orders & Delivery Tracking Dashboard",
        "image": IMG + "642-6d82cb11/screenshot_4_26_2026_12-00-28%20AM.png",
        "url": "https://esrina.maps.arcgis.com/apps/dashboards/766f60fc38594715a0f933f855d6b876#",
    },
    {
        "title": "Benban Solar Farm Monitoring Dashboard",
        "image": IMG + "678-85a64c50/1722524441908.png",
    },
    {
        "title": "Solar Farm Maintenance Tasks Dashboard",
        "image": "/static/images/solar-farms-maintenance-dashboard.png",
        "url": "https://esrina.maps.arcgis.com/apps/dashboards/a6dda17bc6534efe9c91d5891f0644e5#locale=ar",
    },
    {
        "title": "Child Nutrition in Tunisian Schools | WFP",
        "image": "/static/images/school-feeding-tunisia-dashboard.png",
        "url": "https://esrieg.maps.arcgis.com/apps/dashboards/f6e63b20f56c4e3a8a4fb8f7a363e3cf#locale=ar",
    },
    {
        "title": "Running Performance Analytics Dashboard",
        "image": "/static/images/running-analytics-dashboard.png",
        "url": "https://github.com/halaghareeb/running-analytics-dashboard",
        "button_label": "View on GitHub",
    },
]

# ------------------------------------------------------------------ EDUCATIONAL PROJECTS
EDUCATIONAL_PROJECTS = [
    {
        "title": "The Impact of Prior Survey Knowledge and Virtual Global Landmarks on Spatial Knowledge Acquisition",
        "subtitle": "Master’s thesis on wayfinding",
        "paragraphs": [
            "My research examines how prior survey knowledge of a broader environment influences spatial "
            "knowledge acquisition when navigating unfamiliar routes, using a simulated path-following "
            "wayfinding task with first-person video and embedded virtual global landmarks.",
            "Key learnings include designing robust experiments, applying statistical analysis to evaluate "
            "differences, and effectively planning and executing experimental studies.",
        ],
        "image": IMG + "534-addb3651/VGLs_map3.webp",
        "links": [("View", "http://hdl.handle.net/10362/201268")],
    },
    {
        "title": "UAV Study Platform",
        "subtitle": "Monitoring platform for the River Aa in Münster",
        "paragraphs": [
            "We built this platform to showcase the findings and analysis results from the data we collected "
            "with a UAV, such as vegetation health, water quality and flood risk. The platform contains a "
            "dashboard, a wildlife “wiki” page and an embedded ArcGIS StoryMap.",
        ],
        "image": IMG + "533-6e3e880c/Screenshot%202026-04-06%20042232.webp",
        "links": [("View", "https://ifg-uavs.pages.dev/")],
    },
    {
        "title": "Civitas – Malta",
        "subtitle": "Building maintenance platform",
        "paragraphs": [
            "In a group project seminar on programming and analysis, we built a platform to monitor complaints "
            "and the maintenance process, and to present insights from this process on a dashboard. I co-worked "
            "on implementing page components, APIs, the dashboard and statistical visualizations.",
        ],
        "image": None,
        "links": [("View", "https://github.com/pkvartsianyi/civitas")],
    },
]

# ------------------------------------------------------------------ ACHIEVEMENTS
ACHIEVEMENTS = [
    {
        "title": "The Geographic Portal of South Sinai Governorate",
        "tagline": "SAG Award 2024",
        "paragraphs": [
            "During a ceremony, Esri presented the SAG Award to Dr. Khaled Moubarak, Governor of South Sinai.",
            "The project was featured in the national news and is approaching its official launch.",
        ],
        "image": IMG + "589-29bf562f/Screenshot%202026-01-06%20032256.webp",
        "links": [
            ("Article", "https://www.facebook.com/story.php?story_fbid=382611713894363&id=100064366134686"),
            ("Ceremony", "https://www.facebook.com/EsriNorthAfrica/videos/1251783919806776/"),
        ],
    },
    {
        "title": "The Geo-Portal of the Quartz Extraction Project",
        "tagline": "SAG Award 2023",
        "paragraphs": [
            "During the ceremony, Esri presented the SAG Award to the Egyptian Mining Authority at the opening "
            "of the quartz factory in Egypt.",
            "The factory was inaugurated by President Abdel Fattah El-Sisi.",
        ],
        "image": IMG + "591-9e604cd7/Screenshot%202026-04-07%20053743.webp",
        "links": [("View the Esri talk", "https://mediaspace.esri.com/media/t/1_1vmsnv7d")],
    },
    {
        "title": "Egypt Education Smart Map",
        "tagline": "SAG Award 2023",
        "paragraphs": [
            "The project was a collaboration between the Egyptian Ministry of Education and Technical Education "
            "and the World Food Programme (WFP).",
        ],
        "image": IMG + "593-e699de9e/473908503_588419240467201_7673180012096640108_n.webp",
        "links": [("View on the SAG list", "https://events.esri.com/conference/sagList/?fa=List&awardyear=2023")],
    },
    {
        "title": "The Geographic Portal Project of the New Valley Governorate",
        "tagline": None,
        "paragraphs": ["The project was featured in the national news and is approaching its official launch."],
        "image": IMG + "588-4fdbaeda/Screenshot%202026-01-06%20015810.webp",
        "links": [
            ("Article 1", "https://www.youm7.com/story/2022/4/27/%D8%A7%D9%84%D9%88%D8%A7%D8%AF%D9%89-"
                          "%D8%A7%D9%84%D8%AC%D8%AF%D9%8A%D8%AF-%D8%AA%D9%86%D8%AA%D9%87%D9%89-%D9%85%D9%86-"
                          "%D8%A5%D8%AC%D8%B1%D8%A7%D8%A1%D8%A7%D8%AA-%D8%AA%D9%81%D8%B9%D9%8A%D9%84-"
                          "%D8%A7%D9%84%D8%A8%D9%88%D8%A7%D8%A8%D8%A9-%D8%A7%D9%84%D8%AC%D8%BA%D8%B1%D8%A7"
                          "%D9%81%D9%8A%D8%A9-%D8%A7%D9%84%D8%B1%D9%82%D9%85%D9%8A%D8%A9-%D9%84%D9%84%D9%85"
                          "%D8%AD%D8%A7%D9%81%D8%B8%D8%A9/5741941"),
            ("Article 2", "https://www.almasryalyoum.com/news/details/2600446"),
        ],
    },
    {
        "title": "Digital Egypt (“Wasf Masr”)",
        "tagline": "SAG Award 2022",
        "paragraphs": [
            "Esri North Africa and the Information and Decision Support Center (IDSC) received a SAG Award at "
            "the Esri User Conference 2022 ceremony.",
        ],
        "image": IMG + "595-067a25e5/Screenshot%202026-01-06%20042103.webp",
        "links": [
            ("View via Esri NA", "https://www.facebook.com/photo/?fbid=281260021183126&set=a.5953440034723514"),
            ("Article", "https://www.esri.com/partners/information-decision-a2T5x000007dlibEAA/"
                        "description-of-egypt-a2d5x000004Sfd7AAC"),
        ],
    },
]

# ------------------------------------------------------------------ TRAINING AND SKILLS
LIDAR = {
    "title": "LiDAR Training",
    "subtitle": "Data processing experience",
    "paragraphs": [
        "To enrich my knowledge of LiDAR data processing, I used mobile scanning to gain a better understanding "
        "of the nature of LiDAR data (indoor and outdoor), the types of objects that LiDAR can detect and "
        "reflect, and the limitations of the technology when capturing different objects and surfaces.",
        "I then developed my skills further through online courses, where I followed practical tutorials on "
        "generating derivative 3D models and explored LiDAR data classification workflows in ArcGIS Pro. "
        "(Click a picture to enlarge it.)",
    ],
    "images": [
        IMG + "765-7422dc97/WhatsApp%20Image%202026-08-20%20at%207.20.02%20PM.webp",
        IMG + "770-dba8b259/2.jpeg",
        IMG + "767-c55434be/3.webp",
        IMG + "771-e6281e8a/Screenshot%202026-08-21%20012029.webp",
    ],
}

TRAINING_PROJECTS = [
    {
        "title": "Portfolio on ArcGIS Online",
        "subtitle": "Built with ArcGIS Experience Builder",
        "paragraphs": [
            "Building a portfolio with ArcGIS Experience Builder provides an opportunity to explore and experiment "
            "with the different ideas and functionalities available in ArcGIS Online. It also helps develop "
            "greater flexibility in designing interactive and engaging visualizations, while serving as an "
            "effective showcase of the skills and knowledge developed using Esri platforms.",
        ],
        "image": None,
        "links": [("View", "https://experience.arcgis.com/experience/c8445aa7628e42df80222bc555d66aa3")],
    },
]
