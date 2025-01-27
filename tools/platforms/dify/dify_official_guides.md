# GETTING STARTED
## Welcome to Dify
- The Advantage of Dify
- Dify
### Features and Specifications
- Project Basics
- Technical Features
### List of Model Providers

## Dify Community
### Deploy with Docker Compose
### Start with Local Source Code
### Deploy with aaPanel
### Start Frontend Docker Container Separately
### Environment Variables Explanation
### FAQs

## Dify Cloud

## Dify Premium on AWS

# GUIDES
## Model
### Model Types in Dify
- System Inference Models
- Embedding Models
- Rerank Models
- Speech-to-Text Models
### Hosted Model Trial Service
### Setting the Default Model
### Model Integration Settings
- Proprietary Model Providers
- Hosted Model Providers
### Add New Provider
#### Provider Configuration Methods
- Predefined Model
- Customizable Model
- Fetch from Remote
#### Configuration Instructions
- Terminology
- Steps
#### Let's Get Started
- Preparing Provider YAML
- Implement Provider Code
- Custom Model Providers
- Predefined Model Providers
- Adding Models
#### Testing
### Predefined Model Integration
- Preparing the Model YAML
- Implementing Model Invocation Code
### Custom Model Integration
- Writing Vendor YAML
- Writing Model Code
### Interfaces
- Provider
- Model
- LLM
- TextEmbedding
- Rerank
- Speech2text
- Text2speech
- Moderation
- Entities
### Schema
### Load Balancing

## Application Orchestration
### Application Types
- Chat Assistant
- Text Generation
- Agent
- Workflow
### Create Application
- Creating an Application from a Template
- Creating a New Application
- Creating from a DSL File
### Conversation Assistant
#### Applicable scenarios
#### How to compose
- Create an application
- Compose the Application
- Uploading Documentation File
- Debugging
- Publish App
### Agent
- Definition
- Usage Instructions
- Adding Tools for the Agent Assistant
- Agent Settings
- Configuring the Conversation Opener
- Uploading Documentation File
- Debugging and Preview
- Application Publish
### Application Toolkits
- Conversation Opening
- Next Step Question Suggestions
- Citation and Attribution
- Content Moderation
- Annotated Replies
#### Moderation Tool
- Call the OpenAI Moderation API
- Keywords
- Moderation Extension

## Workflow
### Basic Introduction
### Common Use Cases
### Key Concepts
- Nodes
- Variables
- Chatflow and Workflow
### Variables
#### System Variables
- Workflow
- Chatflow
#### Environment Variables
#### Conversation Variables
### Node Description
### Shortcut Key
### Orchestrate Node
#### Serial Node Design Pattern
- Designing Serial Structure
- Viewing Serial Structure Application Logs
#### Designing Parallel Structure
- Parallel Structure Design Pattern
- Designing Parallel Structure Patterns
- Viewing Parallel Structure Application Logs
### File Upload
#### Application Scenarios
#### Difference Between File Upload and Knowledge Base
#### Quick Start: Building a Chatflow / Workflow Application with File Upload Feature
- Method 1: Using an LLM with File Processing Capabilities
- Method 2: Enable File Upload in Application Chat Box (Chatflow Only)
- Method 3: Enable File Upload by Adding File Variables
### Error Handling
#### Application Scenarios
- Handling Network Exceptions
- Backup Workflow Design
- Predefined Error Messages
#### Error Handling Feature
- Not all not supported (LLM, HTTP, Code, Tools)
- Retry on Failure
- Error Handling
#### Quick Start
- Creating a JSON Code Generation Node
- Enable Error Handling Feature for Node A
- Correct the Error Output from Node A
- End
#### Status Overview
- Node Status Types
- Workflow Status Types
#### FAQ
- Before Implementation
- After Implementation
#### Predefined Error Handling Logic
- Logic: None
- Logic: Default Value
- Logic: Fail Branch
- Exception Variables
#### Error Type
- General Error
- Code Node
- LLM Node
- HTTP
- Tool
#### Additional Features
##### Workflow
- Image Upload
##### Chatflow
- Conversation Opener
- Follow-up
- Text-to-Speech
- File Upload
- Citation and Attribution
- Content Moderation
#### Debug and Preview
- Preview and Run
- Step Run
- Conversation/Run Logs
- Checklist
- Run History
#### Application Publishing
- Run App
- Embed into Site
- Access API Reference
- Batch Run App
#### Bulletin: Image Upload Replaced by File Upload

## Knowledge
- Key Advantages
- Use Case
### Create Knowledge
- Create knowledge base
- Choose a chunk mode
- Select indexing method and retrieval setting
#### Reference
- ETL
- Embedding
#### Import Text Data
- Up load local files
##### Import Data from Notion
- Authorize with data provider
- Insert data from Notion Content
- Chunk and clean
- Sync updated pages
- Choose integration configure method (Internal and Public integration)
##### Import Data from Website
- Use third party tools to crawl and parse into Markdown content
- Firecrawl
- Jina Reader
#### Choose a Chunk Mode
##### General Mode
- Chunk indentifier
- Maximum chunk length
- Overlapping chunk length
- Text preprocessing rules
##### Parent-child Mode
- Query Matching with Child Chunks
- Contextual Enrichment with Parent Chunks
##### QA Mode
#### Select the Indexing Method and Retrieval Setting
##### Q2Q and Q2P
##### Setting the Retrieval Setting
- Semantic Retrieval and Keyword Matching
- Vector search, full text search and hybrid
- Vector search: rerank model, top K and score threshold
- Full text search: rerank model, top K and score threshold
- Hybrid search: rerank model, weight setting, top K and score threshold
### Manage Knowledge
- View Linked Applications in the Knowledge Base
- Maintain Knowledge Documents
- Maintain Knowledge Base Via API
#### Maintain Knowledge Documents
##### Manage Documentations in the Knowledge Base
- Adding Documentations
- Disable / Archive / Delete document
##### Managing Text Chunks
- Viewing Text Chunks
- Checking Chunk Quality
- Adding Text Chunks
- Editing Text Chunks
- Modify Text Chunks for Uploaded Documents
- Metadata Management
##### Maintain Knowledge Documents Via API
- Advantages of Utilizing Knowledge Base API
###### API Requesting Examples
- Create a document from text
- Create a Document from a file
- Create Documents from a File
- Create an Empty Knowledge Base
- Get Knowledge Base List
- Delete a Knowledge Base
- Update a Document with Text
- Update a document with a file
- Get Document Embedding Status (Progress)
- Delete a Document
- Get the Document List of a Knowledge Base
- Add Chunks to a Document
- Get Chunks from a Document
- Delete a Chunk in a Document
- Update a Chunk in a Document
- Retrieve Chunks from a Knowledge Base
- Error message
### Integrate Knowledge Base within Application
- Creating an Application Integrated with Knowledge Base
- Connecting Knowledge and Setting Retrieval Mode
- View Linked Applications in the Knowledge Base
### Retrieval Test / Citation and Attributions
- Retrieval Testing
- Citation and Attribution
### Connect to an External Knowledge Base
- Functional Introduction
- Create a Compliant External Knowledge Base API
- Add External Knowledge API
- Connect to the External Knowledge Base
- Test External Knowledge Base and Retrieval Results
- Integrating External Knowledge base in Applications
- Manage External Knowledge
### External Knowledge API
- Endpoint
- Header
- Request Body Elements
- Request Syntax
- Response Elements
- Response Syntax
- Errors
- HTTP Status Codes

## Tools
- Tool Definition
- Functions of Tools
- How to Configure First-party Tools
- First-party Tool Authorization
- How to Create Custom Tools
- Cloudflare Workers
- How to Use Tools in Applications
### Quick Tool Integration
- Prepare the Tool Provider yaml
- Prepare Provider Credentials
- Prepare Tool yaml
- Add Tool Logic
- Add Provider Code
### Advanced Tool Integration
#### Tool Interface
##### Message Return
- Image URL
- Link
- Text
- File BLOB
##### Shortcut Tools
- Text Summary Tool
- Web Page Crawling Tool
##### Variable Pool
- DallE3
- Vectorizer.AI
### Tool Configuration
- Google, Bing, SearchApi, StableDiffusion, Dall-e, Perplexity Search, AlphaVantage
- Youtube, SearXNG, Serper, SiliconFlow, ComfyUI

## Publishing
### Publish as a Single-page Web App
- Web App Settings
- Text Generator Application
- Conversation Application
### Embedding In Websites
- Customizing the Dify Chatbot Bubble Button
- Overriding Default Button Styles
### Developing with APIs
- Benefits of using Dify API
- How to use
- Text-generation application
- Conversational Applications
### Re-develop Based on Frontend Templates
- SDK
- WebApp Template

## Annotation
### Logs and Annotation
- Using the Logs Console
### Annotation Reply
- Workflow
- Enabling Annotated Replies in Prompt Orchestration
- Adding Annotations in the Conversation Debug Page
- Enabling Annotated Replies in Logs and Annotations
- Setting Parameters for Annotated Replies in the Annotation Backend
- Bulk Import of Annotated Q&A Pairs
- Bulk Export of Annotated Q&A Pairs
- Viewing Annotation Hit History

## Monitoring
### Data Analysis
- Total Messages
- Active Users
- Average Session Interactions
- Token Output Speed
- User Satisfaction Rate
- Token Usage
- Total Conversations
### Integrate External Ops Tools
- Why LLMOps Tools Are Necessary
- Prototyping Phase
- Production Phase
- Integrating Dify with Ops Tools
#### Integrate LangSmith
#### Integrate Langfuse
#### Integrate Opik

## Extension
### API-Based Extension
- API Specifications
#### External Data Tool
#### Deploy API Tools with Cloudflare Workers
#### Moderation
### Code-Based Extension
#### External Data Tool
#### Moderation

## Collaboration
- Login Methods
- Creating an Account
### Discover
- Template Applications
- Workspace
### Invite and Manage Members
- Inviting Members
- Removing Members

## Management
### App Management
- Editing Application Information
- Duplicating Application
- Exporting Application
- Importing Application
- Deleting Application
### Team Members Management
- Adding Members
- Member Permissions
- Removing Members
### Personal Account Management
- Login Methods
- Modifying Personal Information
- Login Methods
- Changing Display Language
- View Apps Linked to Your Account
- Delete Personal Account
### Subscription Management
- Upgrading Dify Team Subscription
- Managing Dify Team Subscription
- Frequently Asked Questions

# WORKSHOP
## Basic
### How to Build an AI Image Generation App
## Intermediate
### Build An Article Reader Using File Upload
### Building a Smart Customer Service Bot Using a Knowledge Base
### Generating analysis of Twitter account using Chatflow Agent

# COMMUNITY
## Seek Support
## Become a Contributor
## Contributing to Dify Documentation

# PLUGINS (TODO)
## Introduction
## Quick Start
## Develop Plugins
### Initialize Development Tools
### Tool Plugin
### Model Plugin
### Extension Plugin
### Bundle
## Manage Plugins
## Schema Definition
## Publish Plugins

# DEVELOPMENT (TODO)
## Backend
### DifySandbox
- Contribution Guide
## Models Integration
### Hugging Face
### Replicate
### Xinference
### OpenLLM
### LocalAI
### Ollama
### LiteLLM Proxy
### GPUStack

# LEARN MORE (TODO)
## Use Cases
## Extended Reading
## FAQ

# POLICIES
## Open Source License
## User Agreement

# References
- [1] [Official guides](https://docs.dify.ai/)