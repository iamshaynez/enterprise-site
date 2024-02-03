---
title: "Purposes of Enterprise Architecture"
description: "What makes the concept of benefits and addressing issues so crucial? Introducing a new method into an organization must bring advantages, and this is equally true for Enterprise Architecture (EA)"
summary: "What makes the concept of benefits and addressing issues so crucial? Introducing a new method into an organization must bring advantages, and this is equally true for Enterprise Architecture (EA)"
date: 2024-01-01T16:04:48+02:00
lastmod: 2024-01-01T16:04:48+02:00
draft: false
menu:
  docs:
    parent: ""
    identifier: ""
weight: 120
toc: true
seo:
  title: "Purposes of Enterprise Architecture" # custom title (optional)
  description: "What makes the concept of benefits and addressing issues so crucial? Introducing a new method into an organization must bring advantages, and this is equally true for Enterprise Architecture (EA)" # custom description (recommended)
  canonical: "" # custom canonical URL (optional)
  noindex: false # false (default) or true
---

## Purpose of Enterprise Architecture

### On Books

Text books from the EA discipline usually provide an overview on typical purposes of EAM—also as a motivation. Their authors refer to EAM as a tool to provide transparency by showing processes and also IT applications. We can see an overview of typical purposes in below. Tools provided by EAM can support decisions on the business side—including business process optimisation (left side in below image). They can also support decisions made in solution design, about new software systems or about changes to existing systems (right-hand side in below image). EA and methods promise to support cost reduction by optimising business processes, but also by eliminating redundancy in IT systems, and by supporting faster development of IT systems. If you have a global overview on your business, EA can provide visualisations that help you with improving your business. If you understand your processes and their inefficiencies, then you can improve your processes by performing business process optimisation. If you understood your processes, then you can also deliver software solutions that will perform as expected by business. Textbooks in EA also provide references so we can improve compliance and reduce risk. And last but not least, proper EAM will enable executing the strategy of the corporation.￼

![EAM on book](https://cdn.sa.net/2024/02/03/mZhvfuC3UArLI6k.png)

Do you think that such a kind of list is really helpful in a corporate environment? Just keep in mind you are in a company and people are facing day to day issues with operations and with IT. They are doing a lot of overtime work just by solving current issues. Do you think that you can convince them by promising transparency? Imagine being a consultant and people are stuck with day-to-day routine and you tell them that introducing EA will solve issues by having the big picture. Will this be convincing? Do you think they will immediately tell you that you are hired as a consultant, provide EAM, and then we have transparency and all our problems are solved? Just think about it against the background of your own experience you may have had during internships in companies or by working in companies. Think of your peers, your colleagues or your boss. Which kind of problems do they face and which kind of questions would they expect to have answered by an enterprise architect?

### On Practicality

The application of Enterprise Architecture Management (EAM) in businesses is often subject to criticism. Both in practice and academia, there is a debate over the high-level objectives depicted in below. Are these goals truly beneficial for companies looking to address their challenges? In 2019, over several months, we engaged in unstructured interviews with key decision-makers and architects from a variety of organizations. We questioned them about the daily challenges they face: What issues need addressing? What problems are colleagues asking them to solve? And which of these can be tackled using EA methods and tools?

These interview results were showcased at a conference (see [5]) and also released as a white paper in [6]. A summary of the practitioner-provided topics is illustrated in. A recurring challenge in many companies is identifying which applications are owned. It's not uncommon for a company to struggle with listing all its software applications. Thus, a primary function of EAM should be to maintain an IT inventory that includes all owned applications. Architects need to guide others to more detailed information about these IT applications. Although it may seem elementary, maintaining an up-to-date software inventory remains a significant hurdle for large organizations. Remember that big companies grow over time, often bloated with systems from mergers and acquisitions, and not all systems are universally known. Therefore, building a repository of systems is a crucial starting point for many EA initiatives, which often begin by gathering data on software applications and their users and stakeholders.

![Typical Questions for Enterprise Architects](https://cdn.sa.net/2024/02/03/2xz8J9IfwvyOdVb.png)

Upon initiating an EA project, or when an overview is available, a question frequently posed by the CIO is related to cost savings:
"How can we save money with IT?" While architectural optimization and business support are valuable, the primary goal is often reducing IT expenses. This leads to further inquiries, such as questioning the necessity of certain applications or clarifying their purpose.

These questions may prompt the Enterprise Architect to consider industry standards. Decision-makers, influenced by peers, consultants, or conferences, may inquire about adopting new standards or technologies to achieve cost savings, often within a specific timeframe.

Another fundamental question involves the functionality of an application. Understanding who uses it and its role in supporting business processes is paramount. If applications are deemed necessary, their usefulness must be documented. When looking to cut costs by eliminating redundant applications, the architect must choose the one that best supports the business, potentially phasing out others.

Strategic questions also arise, similar to those discussed in Example 1.2 on page 9. An enterprise architect must be versed in corporate strategy and ensure IT aligns with it. This alignment requires documenting both the strategy and how applications contribute to it, using clear KPIs.

What-if scenarios are another concern ("What if a particular application fails?"). The failure of a critical system can disrupt operations, as illustrated by a hypothetical outage in a parcel logistics company's sorting system. Assessing the importance of applications through impact analysis is therefore essential.

Data protection is a legal requirement, making it critical to know which systems handle personal information. While this sounds straightforward, it becomes complex in organizations with hundreds or thousands of systems. Legal and compliance implications also drive stakeholder interests.

The questions listed in are just a subset of those provided by executives and enterprise architects. The complete list is available in [6], a document that is continuously updated. We also plan to conduct a survey to determine the relative importance of these questions.

### The Purposes

What makes the concept of benefits and addressing issues so crucial? Introducing a new method into an organization must bring advantages, and this is equally true for Enterprise Architecture (EA). Implementing EA necessitates practitioners, an EA team, who will gather information, thereby engaging additional resources (like other employees).
The workflow of an enterprise architect is illustrated in here. It begins with the collection of data regarding information technology (such as infrastructure and software) as well as business elements (like processes and products). This is stored in a specialized database known as an EA data repository. This repository becomes the central point for all types of information, which is regularly updated. Enterprise architects then generate visualizations from this repository, known as viewpoints, for the decision-makers. Imagine a company manager who prefers not to run database queries and sift through obscure data but would rather have visual aids to address their queries.


![Addressing concerns through visualization of business and IT](https://cdn.sa.net/2024/02/03/faiWelpZXNRQLOM.png)


The concerns of stakeholders are the primary motivation for an enterprise architect's activities. We've touched on these concerns when discussing the purpose of EA in the prior Section 1.2. The inquiries presented in image on page 13 are also reflective of stakeholder concerns. Visualizing the IT architecture and the organization's processes helps to address these concerns. Such visualizations are typically derived from the repository—comprising all the data amassed by the Enterprise Architect. As the course progresses, we will delve deeper into the types of data to be collected, the necessary visualizations, and how they can assist in improving the company or satisfying stakeholder needs.

Below screen offers a broad view of typical stakeholder concerns within a corporation. These include operational concerns about effectiveness (quality of outcomes), efficiency (cost reduction), and compliance, as well as strategic IT concerns. These topics will be explored in greater depth in Section 4.1. In the following section, we will present some typical visualizations to give you an idea of how architecture is documented.

![Concerns of EAM](https://cdn.sa.net/2024/02/03/ZFu5nJYHjyEkPsV.png)