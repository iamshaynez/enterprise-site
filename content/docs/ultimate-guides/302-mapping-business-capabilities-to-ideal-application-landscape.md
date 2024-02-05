---
title: "Chatper 3.2 - Mapping Business Capabilities to an Ideal Application Landscape"
description: "Explore how business capabilities drive the ideal IT landscape design for optimal business-IT alignment, emphasizing efficiency and automation support."
summary: "Explore how business capabilities drive the ideal IT landscape design for optimal business-IT alignment, emphasizing efficiency and automation support."
date: 2024-01-01T16:04:48+02:00
lastmod: 2024-01-01T16:04:48+02:00
draft: false
menu:
  docs:
    parent: ""
    identifier: ""
weight: 132
toc: true
seo:
  title: "Chatper 3.2 - Mapping Business Capabilities to an Ideal Application Landscape" # custom title (optional)
  description: "Explore how business capabilities drive the ideal IT landscape design for optimal business-IT alignment, emphasizing efficiency and automation support." # custom description (recommended)
  canonical: "" # custom canonical URL (optional)
  noindex: false # false (default) or true
---

## Mapping Business Capabilities to an Ideal Application Landscape

In this section, we'll delve into the essence of Enterprise Architecture (EA) as it pertains to aligning business operations with IT infrastructure. Our goal is to delineate the steps necessary to design an IT landscape that fully complements the business's needs. To this end, we've previously introduced the concept of business capabilities as a fundamental tool to articulate and comprehend the business segment of an organization (refer to Sect. 2.2). Our next step is to detail how these capabilities can shape an exemplary application landscape.

We approach this by exclusively deriving the landscape from the business capabilities, intentionally disregarding any pre-existing applications. While this may seem impractical given that most companies already have an established suite of applications, our method is intentional in its focus to:

- **Envision an Ideal State:** Crafting a long-term target architecture.
- **Base Decision-Making on Business Needs:** Show how application choices can stem solely from business requirements.

Consider the diagram in Fig below as an illustration of our methodology. It depicts four business capabilities that have been discussed in earlier sections:

![Capabilities and applications](https://cdn.sa.net/2024/02/05/yMXY4C9tchqwHxg.png)

1. **Market Development:** Includes all marketing-related activities.
2. **Logistics Operations:** Encompasses the planning and execution of transport and parcel delivery.
3. **Supplier Management:** Involves monitoring and managing external partnerships.
4. **Customer Support:** Addresses the handling of customer inquiries and issues.

This diagram serves as a typical representation, linking capabilities (at the top) with their respective supporting applications (placed directly beneath each). For instance:

- A CRM system for Market Development,
- A dedicated Logistics system for Logistics Operations,
- A Booking system for Supplier Management,
- A Ticketing system for Customer Support.

What's striking about this layout is the one-to-one relationship between each business capability and its supporting system, eliminating any unnecessary redundancies or overlaps. Each application is designed with a unique functionality set, ensuring no gaps within the landscape. This serves as a prime example of the expected outcome when using our method to derive an ideal application landscape from business capabilities.

The creation of an optimal application landscape to back business capabilities hinges on two key principles:

1. **Automated Capability Support:** Each automated business function should have a corresponding software application.
2. **Redundancy Elimination:** Avoid multiple applications serving the same business capability.

By adhering to the first principle, we ensure that every aspect of the business is effectively supported by IT, maximizing automation potential and delivering high-quality systems. The second principle is about operational efficiency in application support. By sidestepping redundant systems, we reduce operational costs and enable informed decisions to be made about achieving a streamlined yet comprehensive application landscape, balancing cost minimization with robust IT support for automated capabilities.

### Enterprise Architecture Method Summary

This unique enterprise architecture method has been crafted for a global logistics company with a robust IT department capable of developing its own core process software. Figure below provides a visual summary of the method, which will be further detailed in later sections.

![Method of Developing an application architecture](https://cdn.sa.net/2024/02/05/mCcoiBKYrt2jnIQ.png)

#### Initial Procedure: Business Capability Mapping

- **Step 1**: Identify all business capabilities requiring IT support (Fig, Step 1).
  - This is a collaborative decision between business and IT stakeholders, aligned with corporate strategy.
  - 'Application support' implies necessary, but not necessarily fully automated, use of applications.

#### Standardization Assessment

- **Step 2**: Evaluate standardization potential (Fig, Step 2).
  - Considerations include:
    - Uniformity of the capability across the company.
    - Independence of capability from geographic, organizational, or product variations.
    - Consistency of business objects associated with the capability.
  - Benefits of standardization:
    - Lower operational costs due to singular system maintenance.
    - Unified training materials and user education.
    - Simplified integration of new requirements.
    - Consolidated data source, enhancing information accuracy and accessibility.
  - Exceptions to standardization:
    - Legal or physical limitations necessitating diverse software solutions.
    - For instance, distinct customs processing systems per country, or differing mail sorting software for letters versus parcels.

#### Make-or-Buy Decision

- **Step 3**: Determine whether to develop in-house or purchase software (Fig, Step 3).
  - This step applies only to organizations with development capabilities.
  - Standard software typically offers cost efficiency over bespoke solutions.
  - Factors to consider for custom development:
    - Unique business capabilities that provide competitive differentiation.
    - Absence of suitable existing systems in the market.
  - The make-or-buy choice balances business necessity against cost and risk factors.

#### Capability Clustering

- **Step 4**: Group similar capabilities based on decision patterns (Fig, Step 4).
  - Clusters are formed around:
    - Consistency in decisions.
    - Functional relationships.
    - Common business objects.
  - Example: Marketing, sales, and customer service often share customer data, making them a logical cluster for a combined CRM system.

#### Application Landscape Formation

- **Step 5**: Support each cluster with appropriate software applications.
  - Standard capability clusters utilize a single application.
  - Clusters with local adaptations may require multiple applications of the same category.
  - The final landscape may list specific applications (e.g., salesforce.com) or general types (e.g., CRM systems).
