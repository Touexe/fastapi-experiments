# 001

## Overview

This document provides an overview of the "001" project, emphasizing its primary goal of customizing the OpenAPI schema in a FastAPI application. The project incorporates API routes, Pydantic models for user-related data, and custom utility functions designed to modify the OpenAPI schema to specific naming conventions.

## Customization of OpenAPI Schema

The central focus of the "001" project is to tailor the OpenAPI schema to utilize "UserResponse" instead of the default "User[Response]". This customization is achieved through the implementation of the following key components:

### 1. Custom OpenAPI Schema Functions

#### `modify_response_schema_name`

The `modify_response_schema_name` function dynamically adjusts the names of response schemas within the OpenAPI schema. It identifies schemas with titles containing "response" and modifies them to follow the desired naming convention. For example, it transforms "User[Response]" to "UserResponse".

### 2. API Routes and Pydantic Models

While API routes and Pydantic models are integral components of the project, their primary purpose is to support and showcase the customization of the OpenAPI schema. Notably, the project includes API routes under the `/users` endpoint, focusing on retrieving user-related information. Pydantic models such as `UserBaseView`, `UserShort`, and `User` facilitate data validation and representation within the API.

## Project Usage

To observe the customized OpenAPI schema using "UserResponse" naming, run the application using the command `uvicorn main:app --reload` in the terminal. The interactive API documentation is accessible at `/docs`, providing insights into the modified schema.

## Conclusion

"001" serves as a compelling example of leveraging FastAPI to tailor the OpenAPI schema to specific naming conventions. The project's design, coupled with custom functions and data models, demonstrates a structured approach to building web APIs that align with custom specifications for OpenAPI documentation. In this case, it showcases the transformation from "User[Response]" to "UserResponse" for enhanced clarity and consistency in the schema representation.