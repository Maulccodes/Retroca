Retroca README

# 🎮 Retroca

Retroca is an autonomous AI-powered digital product generation platform built with Python, CrewAI, OpenAI, and Streamlit.

The platform uses multiple AI agents working together to:
- discover trending niches
- generate Etsy-ready digital products
- create SEO tags
- generate AI image prompts
- create product images
- export structured product data
- maintain a persistent product database
- manage everything through a live dashboard

---

# 🚀 Features

## 🤖 Multi-Agent AI System

Retroca uses specialized AI agents for:

- Trend Research
- Product Generation
- SEO Optimization
- AI Prompt Engineering

---

## 🎨 AI Product Image Generation

Automatically generates:
- product artwork
- promotional visuals
- digital product mockups

using OpenAI image generation.

---

## 🧠 Persistent AI Memory

Retroca stores generated products inside:

```bash
database/products.json

This enables:

product history
inventory systems
analytics
future duplicate prevention

📦 JSON Product Export

Each generated product exports structured metadata including:

title
description
tags
prompts
image paths

📊 Streamlit Dashboard

Interactive dashboard for:

generating products
browsing generated inventory
viewing AI-generated assets
managing product pipelines

🏗️ Project Architecture
Retroca/
│
├── agents/
│   ├── trend_agent.py
│   ├── product_agent.py
│   ├── seo_agent.py
│   └── prompt_agent.py
│
├── generators/
│   ├── image_generator.py
│   └── json_exporter.py
│
├── utils/
│   ├── file_manager.py
│   └── database_manager.py
│
├── database/
│   └── products.json
│
├── products/
│
├── dashboard.py
├── engine.py
├── tasks.py
├── main.py
└── README.md

⚙️ Installation
1. Clone Repository
git clone https://github.com/Maulccodes/Retroca.git
cd Retroca
2. Create Virtual Environment
python -m venv venv

Activate environment:

Windows
venv\Scripts\activate
Mac/Linux
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt

If requirements.txt does not exist yet:

pip install crewai openai streamlit python-dotenv pillow

🔑 Environment Variables

Create a .env file in project root:

OPENAI_API_KEY=your_openai_api_key

▶️ Running Retroca
Run Dashboard
streamlit run dashboard.py
Run CLI Pipeline
python main.py

🧠 AI Workflow

Retroca follows this generation pipeline:

Trend Agent
    ↓
Product Agent
    ↓
SEO Agent
    ↓
Prompt Agent
    ↓
Image Generator
    ↓
JSON Export
    ↓
Database Memory
📦 Generated Product Output

Each generated product includes:

AI-generated title
Etsy-ready description
SEO keyword tags
AI-generated image
JSON export
saved product folder

📈 Future Roadmap

Planned upgrades include:

Etsy API integration
Automated storefront uploads
Trend analytics dashboard
Product performance scoring
Duplicate detection
ZIP export system
Multi-platform marketplace support
AI pricing optimization
FastAPI backend
React frontend

🛡️ Security

The following files are excluded using .gitignore:

.env
venv/
.venv/
__pycache__/
products/
database/

🧑‍💻 Tech Stack
Python
CrewAI
OpenAI API
Streamlit
JSON
Pillow
dotenv

📜 License

MIT License

👨‍🚀 Author

Built by Maulccodes

Retroca is an experimental AI commerce operating system focused on autonomous digital product generation.
