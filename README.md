# Mattel Limbo AI Prompting
<p align="center">
  <a href="https://fastapi.tiangolo.com/" target="blank"><img src="https://github.com/ferdinalaxewall/mattel-limbo-bot/blob/master/img/banner2-matel-limbo.jpg" alt="Mattel Limbo Logo" /></a>
</p>

**Mattel Limbo** is a Casual AI Prompter designed to generate casual results based on your needs. Our innovative solution leverages cutting-edge technology to provide seamless and intuitive user experiences.

## Introduction

Mattel Limbo aims to simplify the way users interact with AI by providing a casual, user-friendly interface. Whether you're looking for quick answers or creative outputs, our system adapts to your needs effortlessly.

## Available Channel

- **Discord**: Mattel Limbo is a casual AI prompter that integrates with Discord through webhooks. It generates customized responses and sends them as rich embeds, featuring titles, descriptions, and additional fields. The system uses FastAPI to handle incoming requests and processes them to create engaging, AI-generated content tailored to users' needs.

## Installation

```bash
git clone https://github.com/Mattel-Limbo/webhook.git
```

## Running the app
```bash
# Update Dependencies

# Makefile
$ make upgrade

# Default
$ python.exe -m pip install --upgrade pip

# Start Fastapi Server

# Makefile
$ make dev

# Default
$ fastapi dev app.py
```

## Discord Webhook Payload
```json
{
    "username": "",
    "embeds": [
        {
            "author": {
                "name": "",
                "url": "",
                "icon_url": ""
            },
            "title": "",
            "url": "https://google.com/",
            "description": "",
            "color": 15258703,
            "fields": [
                {
                    "name": "",
                    "value": "",
                },
                {
                    "name": "",
                    "value": ""
                }
            ],
        }
    ]
}
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Stay in touch

- Author - [Mattel Limbo](https://github.com/mattel-limbo)
- See all - [Contributors](https://github.com/mattel-limbo/contributors)

## Support Us

If you appreciate our work and want to support the development of Mattel Limbo, consider contributing to our project! You can support us through [Saweria](https://saweria.co/yourlink). Your contributions help us improve and expand our services. Thank you for your support!
