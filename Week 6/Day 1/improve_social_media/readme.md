# Social Media Platform

## Overview
This project is a social media platform designed for a small community. It allows users to post messages, follow other users, and view a timeline of posts from users they follow.

## Features
- **User Registration**: Users can register with unique usernames.
- **Posting Messages**: Registered users can post messages.
- **Following Users**: Users can follow other users.
- **Timeline**: Each user has a timeline of posts from users they follow.

## Structure
The project consists of the following main components:
- **User Class**: Represents a user in the social media platform.
- **SocialMediaPlatform Class**: Manages user registration, posting messages, following users, and generating timelines.
- **PostNode Class**: Used for storing posts in a linked list.

## Flow
1. **User Registration**: Users register with unique usernames using the `register_user` method of the `SocialMediaPlatform` class.
2. **Posting Messages**: Registered users post messages using the `post_message` method of the `User` class.
3. **Following Users**: Users follow other users using the `follow` method of the `User` class.
4. **Timeline**: Each user's timeline is generated using the `generate_timeline` method of the `SocialMediaPlatform` class.

## Usage
To use the social media platform:
1. Create an instance of the `SocialMediaPlatform` class.
2. Register users using the `register_user` method.
3. Allow users to post messages, follow other users, and view their timelines using the provided methods.
