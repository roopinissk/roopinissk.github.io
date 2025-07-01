---
title: Single cell analysis for dummies
date: 2024-06-30
description: single cell tutorial
authors: ["roopini"]
tags:
  - singlecelltutorial
  - singlecellforbeginners
  - single cell basics
---

The past 6 months I have been been learning something new which is single cell transcriptomics. Which is also a method I used in my master thesis. Its quite a complex topic but an extremely interesting one. I am absolutely fascinated and falling in love with. However, while starting I could not get a single tutorial that could help me get started and understand the basics. So, this is my attempt to make a getting started tutorial for absolute beginners. 

### Introduction
What is single-cell analysis?
As the name suggests, it’s literally analysing single cells. In biology, cells divide and replicate their genetic material (DNA and RNA). During this process, DNA is transcribed into RNA, specifically mRNA transcripts, which carry the instructions for producing proteins and regulating cell functions. 

What is the benefit of analysing single cells?
By analyzing these mRNA transcripts, we can understand gene expression at the level of a single cell, which offers insights into cell states, functions, and heterogeneity that bulk RNA-seq can’t capture.

Imagine studying a tumor. In bulk RNA-seq, you get an average signal from all the cancer and surrounding cells. But tumors are made up of many different cell types—some aggressive, some resistant to drugs, and some just regular immune or stromal cells. With single-cell analysis, you can pinpoint which specific cells are driving the cancer’s growth or resisting treatment. This helps in developing more targeted therapies and understanding why some treatments work for certain patients but not others.


### The Method
You might wonder how we isolate and study single cells. In single-cell RNA sequencing (scRNA-seq), the tissue or sample is passed through a microfluidic channel, often with an oil-based medium. This setup encapsulates each cell in an oil droplet. Ideally, each droplet contains:
- One cell
- A bead coated with:
	- A cell-specific barcode (to trace which cell the transcript came from)
    - A UMI (Unique Molecular Identifier) to identify and remove PCR duplicates
- mRNA transcripts released from the cell

Sometimes droplets may contain two or more cells—these are called doublets or multiplets. These can bias your results but are generally removed during computational processing.

There are various platforms for scRNA-seq, such as Smart-seq, Drop-seq, and 10x Genomics Chromium, with 10x Chromium being the most commonly used.

### Analysis
1. How are these saved in a file that is computationally readable?
You can find the data on NCBI GEO 
They can be saved as a FASTQ files or even better prcocessed files in folders which will have the following,
    - barcodes (as a tsv) has all the barcodes
    - features (as a tsv) it has gene id and expression - 90% zeros; it can so be that the gene exp is not available
    - matrix (as mtx) has coordinates of cell in the file

2. What do you need to do inorder to investigate you sample?
The first step would be to download these folders and read them (The code will follow in the next post) and create something called as "objects". Here's how I understood what an object is. Its similar to a dataframe for example, when we read in an excel or a csv, we store is as a dataframe for ease of access. An object is a way the above mentioned data is stored. As you know that there are 3 files-- barcodes, features and matrix all this will be within that object that you create when you read these files together. Now you have all the information from that single cell withing this object. 

![Single cell analysis workflow](/images/image-33.png)

Resources
1. https://web.genewiz.com/faqs/single-cell-rna-seq
2. https://www.singlecellcourse.org/introduction-to-single-cell-rna-seq.html