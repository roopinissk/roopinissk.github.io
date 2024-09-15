---
title: Hadoop Distributed File System
date: 2024-09-15
description: Big Data Analytics
authors: ["roopini"]
tags:

---
# The Hadoop Distributed File System

HDFS is a file storage system. Think of it as a library with several rooms and each room having multiple books, these books that are being held in the shelves can be compared to servers that run the data stored. The way the hdfs stores data within these rooms are different it does not randomly store books. Just like a library would have sections for crime, romance and thriller novels, hdfs has sections for storing the files. 

There are 2 types of data now. the filesystem metadata and the application data. Each of them having dedicated server. 

Filesystem Metadata - namenode

Application metadata - datanode

### Architecture

1. NameNode - think of this as the library receptionist
- the hdfs namespace (this contains the namenode, datanode, inode) is a hierarchy of files and directories which are represented by inodes
- these inodes store data such as the access times, permission, disk space
- The current design has a single NameNode for each cluster. The cluster can have thousands of DataNodes and tens of thousands of HDFS clients per cluster, as each DataNode may execute multiple application tasks concurrently.

1. Image and journal
- in the name space, the inodes and list of blocks is called an image. This image is kept in the RAM by the namenode.
- A persistent record (or a long time storage of data) is stored in the file system called checkpoint.
- the namenode records the changes in a read ahead log called journal in its file system. You can think of this journal as a book record where any changes or damage in a book taken from the library is recorded in a register, any new book taken from the library in entered in this register/ journal
- A library can contain several copies of a single book. Now consider that only one copy of a book remains accessible, the other copies are available only when the original copy is taken or deleted. Now the storage of the several copies of a book will be in a place called checkpoint
- Everytime a library is closed, imagine that the library keeps everything stored in the checkpoint. At the opening of the library, single copies/original book is taken from checkpoint and kept accesible, all this is recorded in the journal

1. DataNodes - think of this as library assistants who report to the namenode
- During startup (when a program is initiated), the datanode connects to the namenode and performs a “handshake” this can be considered a secret code to verify the namespace ID. If the ID does not match that of namenode, then the datanode shuts off and the program is not run.
- A namespace ID is like a unique ID given to the nodes of a specific cluster, nodes of different clusters are given different namespace ID. A newly initialized datanode is allowed to join any cluster and itll take the ID of that particular cluster and cannot be changed.
- The datanode reports everything to the namenode, total storage capacity, fraction of storage in use, and the number of data transfers. The communication is passed as heartbeats and passed with the interval of 3 seconds, if the namenode does not hear back from the datanode in 10 mins, it considers the datanode to be out of service and blocks all replicas. Basically fires the datanode for not doing proper work!
- The namenode constantly replies to the datanode’s hearbeats by giving it instruction— to replicate blocks to other nodes, remove local block replicas, re-register and send an immediate block report, and shut down the node.

To be continued