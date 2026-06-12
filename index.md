---
title: Develop your first agent with Microsoft Foundry
permalink: index.html
layout: home
---

Welcome to the labs for *Develop your first agent with Microsoft Foundry*!

Complete the exercises below in order, to:

1. Set up your environment
1. Create an agent in the Microsoft Foundry portal.
1. Extend your agent in Visual Studio Code
1. Use your agent's endpont in a client application.

> **No Azure Subscription?**<br>Microsoft Foundry is built on Microsoft Azure; so the exercises in this lab require an Azure subscription. If you don't have access to an Azure subscription, but you still want to explore key elements of agent development, you can check out the alternative ***[Explore agent concepts](/Instructions/fallback/99-fallback-lab.md)*** lab; which uses apps with large language models that run locally in your browser - no Azure subscription required!

## Exercises

<hr>

{% assign labs = site.pages | where_exp:"page", "page.url contains '/Instructions/Labs'" %}
{% for activity in labs  %}
{% if activity.lab.title %}

### [{{ activity.lab.title }}]({{ site.github.url }}{{ activity.url }})

{% if activity.lab.level %}**Level**: {{activity.lab.level}} \| {% endif %}{% if activity.lab.duration %}**Duration**: {{activity.lab.duration}}{% endif %}

{% if activity.lab.description %}
*{{activity.lab.description}}*
{% endif %}
<hr>
{% endif %}
{% endfor %}

> **[Ask Anton](https://aka.ms/azk-anton){:target="_blank"}**<br/>![Anton avatar.](./Instructions/Labs/media/anton-icon.png)<br/>If you have questions about some of the topics covered in this lab, *[Ask Anton](https://aka.ms/choose-anton){:target="_blank"}* is a generative AI-based agent that you can ask about AI concepts and Microsoft Foundry. Choose the Azure-based or Browser-based version of the app at **[https://aka.ms/choose-anton](https://aka.ms/choose-anton){:target="_blank"}**. In the Azure-based version, use the **Configure** button to connect the agent to a deployed model in your Foundry project. The browser-based version runs a small language model in your browser, and may run slowly on older or low-spec computers.<br/><br/>*Ask Anton is not a supported Microsoft product or a component of Microsoft Learn or AI Skills Navigator. Just an experimental example of an AI agent for you to explore as you learn about what's possible with AI.*<br/><br/>If you *do* check out Ask Anton, we'd love you to *[tell us about your experience](https://forms.office.com/r/fC0ndfBQeK){:target="_blank"}*!
