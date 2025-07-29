# CIS Vin Decoder

## Overview

The CIS Vin Decoder is a powerful tool designed to decode Vehicle Identification Numbers (VIN) and provide detailed vehicle recall information. This service is tailored for users who require accurate and real-time data on vehicles, leveraging a comprehensive database spanning 40,000 dealerships and over 650 million vehicles across the United States.

## Features

- **VIN Decoding**: The primary function of the CIS Vin Decoder is to decode North American VINs. By inputting at least the first 12 out of the 17 characters of a VIN, users can retrieve detailed vehicle information. This feature is case-insensitive and designed to handle incomplete VIN inputs efficiently.

- **Recall Information**: Alongside VIN decoding, the tool provides recall information when available. This ensures users are informed of any potential safety or compliance issues associated with the vehicle.

## Tool Details

### VinDecode

- **Function Name**: `VinDecode`
- **Description**: Decodes the provided North American VIN and offers recall information if available. A minimum of the first 12 characters of the 17-character VIN is required to attempt a decode. The service is not case-sensitive. Additionally, if the `passEmpty` parameter is set to True, the response will include empty fields in the JSON output.

#### Parameters

- **vin**: 
  - **Type**: String
  - **Description**: The VIN to be decoded. It is not case-sensitive, and the first 12 characters are necessary for decoding.
  
- **passEmpty**:
  - **Type**: Boolean (optional)
  - **Description**: If set to True, empty fields will be included in the response. The default value is False.

## Performance

- **Latency**: 643ms
- **Service Level**: 100%

## Subscription Plans

The CIS Vin Decoder offers a tiered subscription model, providing flexibility based on user needs:

- **BASIC**: Free tier with limited usage.
- **PRO**: $30.00/month for increased limits and additional features.
- **ULTRA**: $60.00/month for even higher limits and premium features.
- **MEGA**: $99.00/month for the most comprehensive access and capabilities.

## Usage

The CIS Vin Decoder is designed for ease of use, enabling users to quickly and efficiently decode VINs and access recall information. Ideal for automotive professionals, dealerships, and vehicle enthusiasts, the tool provides a robust solution for accessing vital vehicle data.

Explore the capabilities of CIS Vin Decoder and leverage its tools to enhance your vehicle data insights and operations.