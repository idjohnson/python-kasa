# System Architecture

This document describes the system architecture of the python-kasa library, which provides a Python interface for controlling TP-Link Kasa and Tapo smart home devices.

## Overview

The python-kasa library is designed to communicate with various TP-Link smart devices including plugs, switches, bulbs, light strips, hubs, and cameras. It provides both a command-line interface (CLI) and a Python library interface.

## High-Level Architecture

```mermaid
graph TD
    A[User Applications] --> B[Python-Kasa Library]
    C[CLI] --> B
    D[FastAPI Server] --> B
    B --> E[Device Discovery]
    B --> F[Device Communication]
    F --> G[Transport Layer]
    F --> H[Protocol Layer]
    G --> I[Device]
    H --> I
    
    style A fill:#f9f,stroke:#333
    style B fill:#bbf,stroke:#333
    style C fill:#f9f,stroke:#333
    style D fill:#f9f,stroke:#333
    style E fill:#fbf,stroke:#333
    style F fill:#fbf,stroke:#333
    style G fill:#ffd,stroke:#333
    style H fill:#ffd,stroke:#333
    style I fill:#ddf,stroke:#333
```

## Core Components

### 1. Device Layer

The device layer represents the physical TP-Link devices that the library communicates with. Different device types are supported:

```mermaid
graph TD
    A[Device] --> B[IOT Devices]
    A --> C[Smart Devices]
    A --> D[SmartCam Devices]
    
    B --> B1[Plug]
    B --> B2[Bulb]
    B --> B3[Strip]
    B --> B4[Dimmer]
    B --> B5[LightStrip]
    B --> B6[WallSwitch]
    
    C --> C1[SmartDevice]
    
    D --> D1[SmartCamDevice]
    
    style A fill:#bbf,stroke:#333
    style B fill:#f9f,stroke:#333
    style C fill:#f9f,stroke:#333
    style D fill:#f9f,stroke:#333
```

### 2. Protocol Layer

The protocol layer handles communication with devices using different protocols based on device type and firmware version:

```mermaid
graph TD
    A[BaseProtocol] --> B[IotProtocol]
    A --> C[SmartProtocol]
    A --> D[SmartCamProtocol]
    
    style A fill:#bbf,stroke:#333
    style B fill:#f9f,stroke:#333
    style C fill:#f9f,stroke:#333
    style D fill:#f9f,stroke:#333
```

### 3. Transport Layer

The transport layer manages the actual network communication with devices:

```mermaid
graph TD
    A[BaseTransport] --> B[XorTransport]
    A --> C[KlapTransport]
    A --> D[KlapTransportV2]
    A --> E[AesTransport]
    A --> F[SslTransport]
    A --> G[SslAesTransport]
    A --> H[LinkieTransportV2]
    
    style A fill:#bbf,stroke:#333
    style B fill:#f9f,stroke:#333
    style C fill:#f9f,stroke:#333
    style D fill:#f9f,stroke:#333
    style E fill:#f9f,stroke:#333
    style F fill:#f9f,stroke:#333
    style G fill:#f9f,stroke:#333
    style H fill:#f9f,stroke:#333
```

## Device Communication Flow

```mermaid
sequenceDiagram
    participant U as User Code
    participant D as Device
    participant P as Protocol
    participant T as Transport
    
    U->>D: device.update()
    D->>P: protocol.query(request)
    P->>T: transport.send(data)
    T->>T: Encrypt/encode data
    T->>D: Send to device
    D->>T: Receive response
    T->>T: Decrypt/decode response
    T->>P: transport.recv()
    P->>D: Process response
    D->>U: Return updated state
```

## CLI Architecture

The command-line interface provides a user-friendly way to interact with devices:

```mermaid
graph TD
    A[kasa command] --> B[CLI Main]
    B --> C[Device Commands]
    B --> D[Discover Commands]
    B --> E[Feature Commands]
    B --> F[Module Commands]
    
    C --> G[on/off/state]
    D --> H[discover]
    E --> I[feature list/set]
    F --> J[module operations]
    
    style A fill:#f9f,stroke:#333
    style B fill:#bbf,stroke:#333
    style C fill:#dfd,stroke:#333
    style D fill:#dfd,stroke:#333
    style E fill:#dfd,stroke:#333
    style F fill:#dfd,stroke:#333
```

## FastAPI Server

The FastAPI server provides RESTful endpoints for controlling devices:

```mermaid
graph TD
    A[HTTP Client] --> B[FastAPI Server]
    B --> C[Auth Validation]
    C --> D[Kasa Command Execution]
    D --> E[Device Control]
    
    style A fill:#f9f,stroke:#333
    style B fill:#bbf,stroke:#333
    style C fill:#dfd,stroke:#333
    style D fill:#dfd,stroke:#333
    style E fill:#ddf,stroke:#333
```

## Module System

Devices support various modules that provide specific functionality:

```mermaid
graph TD
    A[Device] --> B[Module Mapping]
    B --> C[Energy Module]
    B --> D[Light Module]
    B --> E[Schedule Module]
    B --> F[Time Module]
    B --> G[Led Module]
    B --> H[Light Effect Module]
    B --> I[Light Preset Module]
    
    style A fill:#bbf,stroke:#333
    style B fill:#f9f,stroke:#333
    style C fill:#dfd,stroke:#333
    style D fill:#dfd,stroke:#333
    style E fill:#dfd,stroke:#333
    style F fill:#dfd,stroke:#333
    style G fill:#dfd,stroke:#333
    style H fill:#dfd,stroke:#333
    style I fill:#dfd,stroke:#333
```

## Feature System

Features provide a unified interface for device capabilities:

```mermaid
graph TD
    A[Device] --> B[Feature Registry]
    B --> C[State Feature]
    B --> D[Brightness Feature]
    B --> E[Color Temp Feature]
    B --> F[Light Effect Feature]
    B --> G[Signal Level Feature]
    B --> H[Energy Feature]
    
    style A fill:#bbf,stroke:#333
    style B fill:#f9f,stroke:#333
    style C fill:#dfd,stroke:#333
    style D fill:#dfd,stroke:#333
    style E fill:#dfd,stroke:#333
    style F fill:#dfd,stroke:#333
    style G fill:#dfd,stroke:#333
    style H fill:#dfd,stroke:#333
```

## Data Flow in Library Usage

```mermaid
sequenceDiagram
    participant U as User Code
    participant F as Device Factory
    participant P as Protocol
    participant T as Transport
    participant D as Device
    
    U->>F: Device.connect()
    F->>F: Determine device type
    F->>P: Create protocol
    P->>T: Create transport
    T->>D: Connect to device
    D->>U: Return device instance
    U->>D: device.update()
    D->>P: Send query
    P->>T: Send data
    T->>D: Device responds
    T->>P: Receive response
    P->>D: Process response
    D->>U: Updated device state
```