import streamlit as st
from PIL import Image
import smtplib
from email.message import EmailMessage
import base64

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Kowshik BH | Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- CSS FOR STYLING & ANIMATIONS ----------
st.markdown(
    """
    <style>
    /* Hide Streamlit default menu & footer */
    #MainMenu, footer {visibility: hidden;}

    /* Animate headers */
    .stHeader {
        animation: fadeIn 2s ease-in-out;
    }

    /* Keyframes */
    @keyframes fadeIn {
        0% {opacity: 0;}
        100% {opacity: 1;}
    }

    /* Social icon hover effect */
    .social-icon:hover {
        transform: scale(1.2);
        transition: 0.3s ease-in-out;
    }

    /* Dark/light toggle styles */
    .dark-mode {
        background-color: #121212;
        color: white;
    }

    .light-mode {
        background-color: white;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- UTILS ----------

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def display_social_links():
    linkedin_url = "https://www.linkedin.com/in/kowshikbh"
    github_url = "https://github.com/kowshik-bh18"
    leetcode_url = "https://leetcode.com/u/kbh_6281"
    email = "kobh22cs@cmrit.ac.in"

    col1, col2, col3, col4 = st.columns([1,1,1,1])

    with col1:
        st.markdown(f"""
            <a href="{linkedin_url}" target="_blank" title="LinkedIn">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="40" class="social-icon"></a>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
            <a href="{github_url}" target="_blank" title="GitHub">
            <img src="https://cdn-icons-png.flaticon.com/512/733/733553.png" width="40" class="social-icon"></a>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
            <a href="{leetcode_url}" target="_blank" title="LeetCode">
            <img src="https://leetcode.com/static/images/LeetCode_logo_rvs.png" width="40" class="social-icon"></a>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
            <a href="mailto:{email}" title="Email">
            <img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" width="40" class="social-icon"></a>
        """, unsafe_allow_html=True)

def send_email(subject, body, sender_email):
    # Your Gmail SMTP credentials (Use App Passwords for security)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender = "kowshikbh18@gmail.com"  # Replace with your email
    password = "xchq ffbi fazf twlx"   # Replace with your Gmail app password

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = sender
    msg.set_content(body)

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print(e)
        return False

# ---------- SIDEBAR NAVIGATION ----------

st.sidebar.title("Navigation")
pages = ["About Me", "Projects", "Skills", "Contact", "Download Resume"]
choice = st.sidebar.radio("Go to", pages)

# ---------- ABOUT ME PAGE ----------
if choice == "About Me":
    st.title("👋 Hi, I'm Kowshik BH")
    st.markdown("""
    **Address:** BCM Postmetric Boys Hostel, Siddapura, Whitefield, Bengaluru - 560066  
    **Email:** kobh22cs@cmrit.ac.in | kowshikbh18@gmail.com  
    **Mobile:** +91 9110868186  
    """)
    st.write("---")
    st.subheader("Career Objective")
    st.write("""
    - Actively seeking a dynamic IT role as Software Developer or Web Developer at a forward-thinking company.  
    - Bringing a robust skill set in web and software development, strong work ethic, effective leadership, and adaptability.  
    - Enthusiastic about collaborating with experienced professionals to enhance skills and knowledge.  
    """)
    st.write("---")
    st.subheader("Education Qualification")
    st.markdown("""
    - B.E. Computer Science & Engineering, CMR Institute of Technology, Bengaluru  
      CGPA - 8.9 (2026 - Pursuing)  
    - 12th Grade - Science, BGS Independent PU College, Mandya (97%)  
    - 10th Grade, Sri Bhakthanatha Swamy High School, Mandya (93%)  
    """)
    st.write("---")
    st.subheader("Personal Details")
    st.markdown("""
    - **Date of Birth:** 3rd March 2004  
    - **Gender:** Male  
    - **Nationality:** Indian  
    - **Permanent Address:** Near Venugopala Temple, Bindenahalli, Nagamangala, Mandya, Karnataka - 571445  
    - **Languages:** English (Full professional proficiency), Kannada (Native), Hindi (Limited working proficiency)  
    - **Hobbies:** Listening to soundtracks, playing cricket and kabaddi  
    """)
    st.write("---")
    st.subheader("Connect with Me")
    display_social_links()

# ---------- PROJECTS PAGE ----------
elif choice == "Projects":
    st.title("🚀 Projects")

    # Project 1 - Dormitory Management System
    st.markdown("""
    ### Dormitory Management System
    Web-based app to automate hostel administrative tasks including room allocation, attendance, visitor management, fee collection, and reporting.
    - **Technologies:** HTML, CSS, JavaScript, Django, MySQL  
    - **GitHub:** [Dormitory Management System](https://github.com/Kowshik-bh18/Dormitory_Management_System)  
    """)

    # Project 2 - Gym Management System
    st.markdown("""
    ### Gym Management System
    Software application to manage gym operations: member info, staff details, scheduling, billing, inventory, and reporting.
    - **Technologies:** HTML, CSS, JavaScript, Tkinter, Django  
    - **GitHub:** [Gym Management System](https://github.com/Kowshik-bh18/Gym_Management_System)  
    """)
    
    st.write("---")
    st.subheader("More projects coming soon...")

# ---------- SKILLS PAGE ----------
elif choice == "Skills":
    st.title("💡 Technical Skills")
    st.markdown("""
    - **Programming Languages:** Python, Java, JavaScript, C  
    - **Web Technologies:** HTML, CSS, Bootstrap, Django  
    - **Databases:** PostgreSQL, MySQL, MongoDB  
    - **Cloud & DevOps:** Google Cloud Platform (GCP), Basic DevOps Practices, CI/CD (Beginner)  
    - **Scripting:** Bash Scripting  
    - **Tools:** Linux, Git, GitHub, VS Code, Solid Edge, Microsoft Excel, PowerPoint  
    """)
    st.write("---")
    st.subheader("Achievements & Activities")
    st.markdown("""
    - Led team to victory in Taluk-level Kabaddi competition (Leadership & teamwork)  
    - Selected Top 10 teams in IGNITEX 2025 Hackathon (Innovation & problem-solving)  
    - 2nd place in KGF Kannada competition at Cultura 2024 (Creativity & linguistic skills)  
    - Certified Python & Django Bootcamp (Udemy)  
    - Completed JavaScript, C, Java courses (Udemy)  
    - Workshops: Data Science, Data Visualization  
    - Active member of Samskruthi Kannada Club  
    """)

# ---------- CONTACT PAGE ----------
elif choice == "Contact":
    st.title("📬 Contact Me")
    with st.form(key='contact_form'):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit = st.form_submit_button("Send Message")

        if submit:
            if name and email and message:
                sent = send_email(
                    subject=f"Portfolio Contact from {name}",
                    body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                    sender_email=email
                )
                if sent:
                    st.success("✅ Message sent successfully! I will get back to you soon.")
                else:
                    st.error("❌ Failed to send message. Please try again later.")
            else:
                st.warning("⚠️ Please fill all the fields.")

    st.write("---")
    st.subheader("Or connect directly via:")
    display_social_links()

# ---------- DOWNLOAD RESUME PAGE ----------
elif choice == "Download Resume":
    st.title("📄 Download Resume")
    with open("resume.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    b64 = base64.b64encode(PDFbyte).decode()
    href = f'<a href="data:file/pdf;base64,{b64}" download="Kowshik_BH_Resume.pdf">📥 Click here to download my Resume</a>'
    st.markdown(href, unsafe_allow_html=True)

# ---------- DARK / LIGHT THEME TOGGLE ----------
if 'theme' not in st.session_state:
    st.session_state['theme'] = 'light'

def toggle_theme():
    if st.session_state['theme'] == 'light':
        st.session_state['theme'] = 'dark'
    else:
        st.session_state['theme'] = 'light'

st.sidebar.button(
    "Toggle Dark/Light Mode",
    on_click=toggle_theme
)

if st.session_state['theme'] == 'dark':
    st.markdown(
        "<style>body {background-color: #121212; color: white;}</style>",
        unsafe_allow_html=True
    )
else:
    st.markdown(
        "<style>body {background-color: white; color: black;}</style>",
        unsafe_allow_html=True
    )
