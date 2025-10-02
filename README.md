# Neuron Chat

## 📝 Preface

Hello! I'm the Author of this Project, and I want to be transparent about my journey with this project. I'm still learning and developing my skills as a programmer, and I'm using AI assistance to help guide me through this development process. This isn't about AI finishing my code for me - rather, it's about learning from AI as a mentor and teacher while I build something meaningful. Every line of code here represents my learning journey, with AI serving as a helpful companion along the way.

> A modern, local AI-powered chat application that enables private conversations with AI models without relying on cloud services.

## 🚀 Overview

Neuron Chat is a privacy-focused, desktop AI chat application built with Python and CustomTkinter that enables users to have intelligent conversations with local AI models. This application allows users to feel the Power of AI while ensuring complete privacy and data control by running everything locally.

## ✨ Features

- 🤖 **Local AI Processing** - Powered by Hugging Face Transformers with distilgpt2 model for text generation (coming soon more models and better integration)
- 🔒 **Privacy First** - All conversations stay on your device
- 💬 **Intuitive Chat Interface** - Clean, modern desktop GUI built with CustomTkinter
- ⚡ **Fast & Responsive** - Lightweight Python application with efficient database storage
- 🎨 **Customizable** - Modern CustomTkinter theming with light/dark mode support
- 📱 **Cross-Platform** - Runs on Windows, macOS, and Linux

## 🛠️ Technology Stack

- **Frontend**: Customtkinter (https://customtkinter.tomschimansky.com/)
- **Backend**: Python 3.8+
- **AI Integration**: Hugging Face Transformers (distilgpt2 model)
- **Database**: Default: PostgreSQL
- **Other**: SQLAlchemy ORM, python-dotenv for configuration

## 📋 Prerequisites

Before running Neuron Chat, ensure you have:

- Python 3.8+ installed on your system
- PostgreSQL database (for conversation storage)
- At least 2GB RAM (for AI model loading)
- Internet connection (for initial model download)

## 🚀 Installation

### Quick Start

```bash
# Clone the repository
git clone https://github.com/Keidel187/neuron-chat.git
cd neuron-chat

# Install Python dependencies
pip install -r requirements.txt

# Install additional AI dependencies
pip install transformers torch
```

### AI Model Setup

The application uses Hugging Face's distilgpt2 model, which will be automatically downloaded on first run.

```bash
# Set up environment variables for database (optional)
cp .env.example .env  # Create from template if needed
# Edit .env with your PostgreSQL credentials
```

## 🖥️ Usage

### Starting the Application

```bash
# Start the application
python main.py
```

### Basic Usage

1. Launch the application using `python main.py`
2. The AI model will load automatically on first startup
3. Use the chat interface to interact with the AI assistant

### Configuration

Configure database connection and other settings using environment variables:

```env
# Database Configuration
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
POSTGRES_DB=neuron_chat
DB_HOST=localhost
DB_PORT=5432
```

## 📸 Screenshots

*Screenshots will be added as the UI development progresses*

```
[Main chat interface - Coming soon]
[AI conversation view - Coming soon]
[Settings panel - Coming soon]
```

## 🔧 Development

### Setting up Development Environment

```bash
# Clone the repository
git clone https://github.com/Keidel187/neuron-chat.git
cd neuron-chat

# Install dependencies including development tools
pip install -r requirements.txt

# Set up PostgreSQL database
# Create database and configure .env file
```

### Building from Source

```bash
# The application is currently in development
# Building/packaging instructions will be added later
python main.py  # Run directly from source
```

### Running Tests

```bash
# Run tests using pytest
pytest tests/

# Run tests with verbose output
pytest tests/ -v
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 Python coding standards
- Use meaningful commit messages
- Ensure code is well-documented with docstrings
- Run tests before submitting PR: `pytest tests/`
- Test changes manually before submitting PR

## 📝 Roadmap

- [ ] Complete chat interface UI implementation
- [ ] Add support for multiple AI models (GPT, LLaMA, etc.)
- [ ] Implement conversation history and management
- [ ] Add settings panel for customization
- [ ] Implement export/import functionality for conversations
- [ ] Add plugin system for extensions

## ❓ FAQ

**Q: Do I need an internet connection to use Neuron Chat?**
A: Only for the initial setup to download the AI model. After that, everything runs locally.

**Q: What AI models are supported?**
A: Currently using distilgpt2 from Hugging Face. More models will be added in future releases.

**Q: Is my conversation data safe?**
A: Yes, all conversations are stored locally in your PostgreSQL database and never sent to external servers.

## 🐛 Troubleshooting

### Common Issues

- **Issue**: ModuleNotFoundError for transformers or torch
  - **Solution**: Run `pip install transformers torch` to install AI dependencies

- **Issue**: Database connection errors
  - **Solution**: Ensure PostgreSQL is running and environment variables are correctly set in .env file

- **Issue**: AI model fails to load
  - **Solution**: Check internet connection for initial model download, ensure sufficient RAM (2GB+)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Keidel187**

- GitHub: [@Keidel187](https://github.com/Keidel187)

## 🙏 Acknowledgments

- Inspiration: https://github.com/chatboxai/chatbox
- Hugging Face for providing excellent AI models and transformers library
- CustomTkinter community for the modern GUI framework

## 📊 Project Status

Active Development

---

*Last updated: 02.10.2025*
