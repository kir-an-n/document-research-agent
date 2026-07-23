# Autonomous Document Research Agent

An agent that reasons over multi-step tasks by deciding which tools to call and when — built to combine OCR, retrieval, and computation into a single reasoning system, rather than answering from a fixed single-step pipeline.

## The Problem

Most RAG systems answer a question in one shot: retrieve, then generate. But many real tasks need multiple steps — extract text from a scanned document, then look something up, then compute something with it. This project explores building a genuinely agentic system: one that decides *which tool to use, in what order*, based on the task at hand, rather than following a hardcoded sequence.

## What This Project Does (so far)

1. Defines tools the agent can call (starting with a calculator; OCR and retrieval to follow)
2. Uses an LLM (Llama 3.3 70B via Groq) with function-calling to decide, per query, whether a tool is needed and which one
3. Executes the chosen tool and returns its result, or answers directly if no tool is needed

## Current Status: Early Stage

This project is in active development. Right now it has:
- A working agent loop that correctly distinguishes between questions needing a tool (e.g., math) and questions it can answer directly from its own knowledge
- One tool implemented: a calculator

**Planned next steps:**
- Wire in OCR (reusing the BillSmart pipeline) as a callable tool
- Wire in document retrieval (reusing the adaptive-chunking-rag pipeline) as a callable tool
- Support multi-step tasks that chain 2+ tools together (e.g., "OCR this document, then answer a question about it")
- Add citations so answers point back to their source
- Build an evaluation harness measuring task success rate across a set of realistic multi-step queries

## Example (current capability)
