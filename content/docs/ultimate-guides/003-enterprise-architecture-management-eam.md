---
title: "Chatper 1.3 - Enterprise Architecture Management (EAM)"
description: "Explore Enterprise Architecture Management (EAM): a strategic approach to align IT infrastructure with business goals. Learn methodologies, tools, and best practices for transitioning to optimal enterprise architecture."
summary: "Explore Enterprise Architecture Management (EAM): a strategic approach to align IT infrastructure with business goals. Learn methodologies, tools, and best practices for transitioning to optimal enterprise architecture."
date: 2024-01-01T16:04:48+02:00
lastmod: 2024-01-01T16:04:48+02:00
draft: false
menu:
  docs:
    parent: ""
    identifier: ""
weight: 113
toc: true
seo:
  title: "Enterprise Architecture Management (EAM)" # custom title (optional)
  description: "Explore Enterprise Architecture Management (EAM): a strategic approach to align IT infrastructure with business goals. Learn methodologies, tools, and best practices for transitioning to optimal enterprise architecture." # custom description (recommended)
  canonical: "" # custom canonical URL (optional)
  noindex: false # false (default) or true
---

## Enterprise Architecture Management (EAM)

The preceding segments have offered a concise summary of Enterprise Architecture (EA) and how it is depicted. These parts tackled inquiries such as: What are the ways to represent business and IT? The instances given were intended to serve as a brief prelude, with a promise of more detailed visual representations in the following chapters.

### Enterprise Architecture Management Explained

Before diving deeper into the methodologies and tools, it's important to clarify what we mean by EAM. EAM is essentially about capturing the current IT environment and its business relationships over time. It's not just about understanding the present state, but also about transitioning from this current 'as-is' state towards a more refined 'to-be' architectural vision. EAM serves as a disciplined process for both establishing and continually updating the blueprints that illustrate the intersections of business operations and technological infrastructure. Moreover, it ensures that IT strategies are in lockstep with the broader business goals that the organization aims to achieve. In practice, EAM delivers a set of methodologies, establishes organisational frameworks, and promotes best practices. These are instrumental in implementing and executing enterprise architecture initiatives within a business setting.

Enterprise Architecture Management (EAM) is the methodical process of establishing, updating, and applying enterprise architecture to ensure the synchronization of IT with business objectives. EAM lays out the necessary methodologies and organizational structures to facilitate effective enterprise architecture functions.

### Enterprise Architecture Management and Interrelated Fields

As we conclude Chapter 1, a foundational comprehension of Enterprise Architecture (EA) and Enterprise Architecture Management (EAM) should now be established. It's essential to remember that EAM isn't a panacea for all organizational challenges or a one-size-fits-all approach to business management. We've already touched upon several management practices that are being utilized in businesses and are the focus of scholarly studies.

![The relationship between EAM and other management disciplines](https://cdn.sa.net/2024/02/04/F1IUTgX63mYMSVr.png)

Project portfolio management is one such discipline. Corporations manage a myriad of projects with intricate interdependencies, necessitating astute decisions about which projects to undertake immediately and in what sequence. Additionally, there's the technical domain of IT infrastructure management. Despite EAM's aspirations to offer a comprehensive framework, it isn't intended to supersede these existing fields. Specifically, EAM relies on inputs from strategic planning, which continues to provide techniques and instruments for dissecting a business's environment, markets, etc., and for making deliberate choices about future actions. These strategic determinations then become fodder for EAM initiatives.

EAM's domain encompasses IT and software applications, influencing the approach to IT infrastructure management, though it is not a component of EAM itself. There are unique facets to IT infrastructure management that extend beyond our EAM dialogue, yet the overlap between the two is considerable. The situation is similar with project portfolio management. We've identified potential modifications within the corporate software landscape, such as deploying new systems, decommissioning outdated ones, adapting current systems to new demands, or consolidating separate applications into a unified platform. Each alteration is executed within a project's framework. EAM adopts a bird's-eye view, not limiting itself to a single project but overseeing a suite of projects. This holistic perspective integrates methodologies and tools from project portfolio management. Thus, managing a company isn't about employing a singular set of tools; rather, EAM operates in tandem with other disciplines, aiding in the harmonization of business and IT objectives while offering insights and decisions that bolster the efficacy of these other disciplines.

### Architectural Layers

The concept of dividing an enterprise's architecture into separate "layers" is universally adopted across various methods and Enterprise Architecture (EA) frameworks. This approach is rooted in the "divide and conquer" principle, which suggests handling the architecture not as a monolithic entity, but rather by segmenting it into digestible, interconnected layers or perspectives.

In our textbook, we adopt a straightforward layering model, depicted in below. At the top of this model sits the **Business Architecture** (or Business Layer), which encompasses all elements that define the business. Examples of these elements include business processes, strategies, Key Performance Indicators (KPIs), objectives, and goals—all critical in painting a picture of the business landscape. We will dive deeper into this topic in Chapter 2. Enterprise architects commonly invoke the term "business architecture" when discussing their comprehensive understanding of the business.  

![Common Enterprise Architecture Layers](https://cdn.sa.net/2024/02/04/6dspmg1orDTnBMt.png)

Positioned beneath the business architecture is the **Application Architecture** (or Application Layer). This layer is the collective representation of all the software applications an organization uses and maintains. It extends to the data residing within these applications, the data flows, and the interfaces linking the applications. Application landscapes in the real world are often expansive and complex, and these intricacies are encapsulated within the notion of application architecture. Chapter 3 will explore this layer in detail.

Distinct from the first two layers, the **Technology Architecture** (or Technology Layer) is another critical layer. It includes all the hardware and IT infrastructure components such as networks, data centers, and the physical locations necessary for establishing and maintaining IT systems. This layer is decidedly technical in nature.

While traditional EA frameworks may present additional layers and a more intricate structure, our simplified tri-layer model—distinguishing between business, applications, and IT technology—adequately serves our purposes.

This book will not delve into the nuances of technology architecture, IT infrastructure, or IT service management. Instead, our focus will be on:
- Describing the business architecture as the topmost layer in Figure 1.20 (Chapter 2).
- Elucidating the application architecture (Chapter 3).
- Exploring the interconnections between business concepts and application architecture (Chapter 4).
- Strategizing future changes within the application architecture (Chapter 5).