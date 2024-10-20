---
title: Chatper 2.1 - Business Processes Guide
description: Explore Business process in business architecture of Enterprise Architecture
  Management (EAM).
summary: Explore Business process in business architecture of Enterprise Architecture
  Management (EAM).
date: 2024-01-01 16:04:48+02:00
lastmod: 2024-01-01 16:04:48+02:00
draft: false
menu:
  docs:
    parent: ''
    identifier: ''
weight: 121
toc: true
slug: chatper-21-business-processes-guide
---


# Business Processes

Before we delve any deeper, let's clarify what we mean by business processes. While this book isn't a replacement for a full-fledged course on business process management, it will give you enough insight to grasp the basics of business processes. As we progress, we'll connect the dots between business processes and other key concepts in business architecture.

![Business process and process map](https://cdn.sa.net/2024/02/04/oYaR5xcnjzIXSiv.png)

## What is a Business Process?

A business process is essentially a sequence of tasks or activities carried out within an organization. It's bound by time, with a specific start and end point. Execution of these processes typically requires resources, such as:

- Human effort: People completing tasks.
- Machinery: Tools and equipment operated by personnel.
- Technology: Fully automated systems functioning without direct human intervention.

Business processes are not confined to the corporate world; they're part of our daily lives. However, within the scope of this text, we focus on processes in a commercial setting, where the following aspects are pivotal:

- **Cost**: Implementing business processes incurs expenses.
- **Efficiency**: The goal is often to minimize costs without compromising quality.

### The Goal of Business Process Optimization

When professionals discuss business processes, especially in the context of optimization, they're essentially looking at ways to save money. Optimization might involve streamlining activities, improving coordination between departments, or leveraging technology to reduce the need for manual input.

Stay tuned as we explore how these processes fit into the broader framework of business architecture and contribute to an organization's overall efficiency and profitability.

## Understanding Business Process Maps

### Defining Business Process vs. Process Map

It's essential to distinguish between a business process and a process map. A **business process** is the actual sequence of tasks performed in a company. In contrast, a **process map** is a visual or textual representation of this sequence. If you've ever worked with process maps or seen them in business process modeling textbooks, or encountered them during an internship, you're aware that they are integral to guiding employees on how to execute their tasks.

### Visibility and Purpose of Process Maps

While you can observe the hustle and bustle of a shop floor, with its machinery, materials, and busy personnel, the business processes themselves are not directly visible. To make these processes understandable, we create process maps. These maps serve as comprehensive guides for those unfamiliar with the work, enabling them to follow a process step by step.

### Role in Business Process Management

Business process maps are invaluable for **corporate business process management**. You can only manage what you fully grasp, and process maps provide the necessary documentation for this understanding. They play a critical role in process improvement; ensuring not just that processes are operational, but that they are also optimized and enhanced over time. For process automation, these maps are utilized as blueprints, supported by **Business Process Management Systems (BPMS)** or **Workflow Management Systems (WfMS)**, which require a formal process description to automate business process execution.

### Characteristics of Business Processes

Business processes are transformative by nature, as depicted in **below**. They are not aimless tasks but are geared towards producing valuable outcomes for customers. Consider car manufacturing: the car (output) provides value to the customer, but its production requires inputs like materials and parts. These inputs are transformed into the final product.

![Properties of a Business Process](https://cdn.sa.net/2024/02/04/dGcgCjWXDVpuLYk.png)

### Continuity and Complexity in Processes

Business processes are typically recurring activities, not one-off projects. Mapping makes sense only if the process will be repeated and remains relevant. These processes often have inherent complexity, with multiple decisions influencing the flow.

### Alignment with Corporate Strategy

A business process must align with the company's overall strategy. For instance, a car manufacturing process fits a car manufacturer's strategy, not a logistics company focused on delivering parcels. Each company will prioritize processes that support its unique strategy.

### Visualizing Business Processes

Those experienced with business processes may be familiar with various visualizations, or **business process models**. Globally, methods to describe a business process vary widely. They can be captured in text, specialized tools, standardized languages, or even through a sequence of symbols on presentation slides.

## Business Process Management and Enterprise Architecture Management

### Understanding Business Processes
Business processes are integral to how a company functions, and many organizations have adopted Business Process Management (BPM) to standardize and enhance these processes. BPM tools often include process maps, which serve as a baseline for improving and managing a business's workflow. My personal experience began in logistics, where I was recruited to implement business process modeling. However, upon starting, I found myself part of the business architecture team, with the task of aiding in process modeling so these models could be transitioned to the enterprise architects.

Initially, there was an absence of detailed business process maps, and our role was to assist business experts in articulating their processes uniformly. The expectation was that business personnel would recognize the value of these maps for communication and operational clarity.

### The Challenges of Detailed Process Maps
Creating detailed process maps is not trivial—it's a considerable undertaking. The process involves months or even years of interviews across departments, documenting workflows, and validating the information. Here are some of the key challenges:

![The Challenges of Detailed Process Maps](https://cdn.sa.net/2024/02/04/71HGws5CUuzEeXd.png)

- **Effort and Time**: Documenting processes is labor-intensive, requiring extensive collaboration with business experts.
- **Maintaining Relevance**: Keeping these maps current is crucial; as processes evolve due to internal optimizations or external factors, maps must be updated accordingly.
- **Resistance to Transparency**: There is often pushback against change and a reluctance to reveal work procedures for fear of job redundancy or exposing simplicity in tasks.
- **Silo Mentality**: Departments may guard their processes closely, fearing loss of control or unwanted interference if their methods become too transparent.

### The Quest for Less Detail in EAM
For an effective Enterprise Architecture Management (EAM), a less granular overview of business activity is necessary. The focus is on understanding what the company does rather than the intricate details of how each process is executed. This is akin to the role of a town planner who is concerned with the macro layout rather than the interior design specifics of buildings.


### Streamlining the Application Landscape
In designing a corporate application landscape, the goal is to avoid purchasing redundant software by consolidating functionalities. Reducing duplicate processes is also a priority, and detailed business process information can sometimes be a hindrance, providing unnecessary or even misleading input.

Below contrasts the level of detail in business process models with the requirements for EAM:

![Level of detail provided by process models compared requirements for EA](https://cdn.sa.net/2024/02/04/OuSMR8qspatdkYH.png)

- **For EAM**: High-level information about systems and their relation to business concepts is required.
- **For BPM**: Detailed instructions, actor responsibilities, execution sequences, decision-making, and loops are described.

### High-Level Business Concepts for EAM
In managing software applications, information is needed not at the user level but rather on organizational units or roles. Interfaces, data exchanges, and service provisioning will be discussed in Chapter 3. Strategic resources and general business concepts are the focus, with a detailed look at strategy, objectives, and Key Performance Indicators (KPIs) in Sections 2.3 and 2.4 to measure achievement.

The concept of a 'business capability' is a fundamental notion in EAM and will be elaborated on in the following sections of the document.