---
title: "Chatper 3.4 - Data Architecture Overview"
description: "Explore the integration of data architecture within enterprise architecture, covering business processes, application relationships, and technology implementation. Understand the significance of business objects and data models in aligning software development with business concepts."
summary: "Explore the integration of data architecture within enterprise architecture, covering business processes, application relationships, and technology implementation. Understand the significance of business objects and data models in aligning software development with business concepts."
date: 2024-01-01T16:04:48+02:00
lastmod: 2024-01-01T16:04:48+02:00
draft: false
menu:
  docs:
    parent: ""
    identifier: ""
weight: 134
toc: true
seo:
  title: "Chatper 3.4 - Data Architecture Overview" # custom title (optional)
  description: "Explore the integration of data architecture within enterprise architecture, covering business processes, application relationships, and technology implementation. Understand the significance of business objects and data models in aligning software development with business concepts." # custom description (recommended)
  canonical: "" # custom canonical URL (optional)
  noindex: false # false (default) or true
---

## Data Architecture Overview

Remembering the EA structure which includes:

- **Business Architecture**: This layer focuses on:
  - Business processes
  - Organizational capabilities
  - Business objects
  - Other business-centric concepts
- **Application Architecture**: This involves:
  - Applications
  - Inter-application relationships
- **Technical Architecture**


While we've largely discussed business objects, they're pivotal as a foundation for deriving data models that are crucial for applications and software development. The term "data architecture" does pop up in some frameworks; however, we're not modifying our three-tiered model to add an extra layer. Instead, we'll integrate the concept of data into the existing structure.

Data architecture refers to the handling of data at various levels of detail within an enterprise, as depicted in Fig below. Business objects from the business architecture provide a business-centric view of data. In application architecture, data objects symbolize data managed and transferred between applications. At the technology level, databases represent business objects.

![Data architecture](https://cdn.sa.net/2024/02/05/2iEwWe5kOXNPg1h.png)

### Data Architecture: A Cross-Sectional Perspective

We won't delve deeply into data architecture in this textbook, but it's important to acknowledge its existence and the variability in its interpretation. For us, data architecture is a distinct dimension that spans all layers, with specific representations at each abstraction level:

- **Business Architecture**: Business objects represent high-level business data.
- **Application Architecture**: Data objects provide a detailed perspective on data.
- **Technology Implementation**: Concrete application systems utilize databases to make data persistent.

All these elements represent data but differ in their level of abstraction (Fig below). Business objects, at the highest level, capture key business terms and can include natural language descriptions and properties. The Business Object Model (BOM) depicts their interrelations, driven by business terminology.

![level of abstraction of data architecture](https://cdn.sa.net/2024/02/05/baYf2CVmkdMcutA.png)

### From Business Objects to Data Implementation

The BOM can initiate the creation of an application-specific data model, an essential tool for software development that supports software engineers in design and implementation. It should align with the BOM and reuse its terms, detailing data objects, attributes, and their interconnections.

The data model must resonate with business stakeholders, avoiding abstract programming terms in favor of recognizable business concepts. It extends to include new data types necessary for system realization without delving into implementation specifics at the business layer.

At the technology architecture level, databases are materialized with intricate details like primary and foreign keys, tables, and relationships—information that's overly technical for the business layer but essential for database design. Transitioning from the BOM through the data model to the database introduces increasing technical details necessary for system implementation.
