# 2021 - Artown Project

2022년 2학기 데이터베이스시스템 과목의 기말 프로젝트입니다.

## Description

**Project Name :** Artown

Art(예술) + Town(도시, 모임) = Artown : Artist(예술가)들의 모임!

아트타운은 예술 활동을 무겁고 어렵게 생각하는 사람들을 위해 가볍게 삶에서 예술 활동을 할 수 있도록 하는 서비스입니다. 또한 무명 예술가들의 전시 공간을 제공해 주는 역할을 합니다.

기본적으로 instagram 시스템을 참고하여 제작 되었습니다.

## Function

- 회원가입, 로그인, 로그아웃
- 예술품 탐색
- 예술품 업로드, 편집, 삭제
- 댓글 작성, 편집, 삭제

## System architecture

**Activity Diagram**
![그림1](https://user-images.githubusercontent.com/86937253/209667600-6f1e8273-ef74-497f-95a4-d96c1991e8d1.png)

**User Case Diagram**
![그림2](https://user-images.githubusercontent.com/86937253/209667728-dbaf0fd7-4779-468b-9bf7-fb1c50827838.png)

**ER-Diagram**
![그림3](https://user-images.githubusercontent.com/86937253/209667810-479938f1-cc77-4f39-b1f9-775fe2335509.png)

## Environment

**CSS Framework :** Bootstrap
**Web Framework :** Django
**Database sys :** SQLite

## Prerequisite

**requirements**
asgiref==3.5.2
Django==4.0.4
Pillow==9.1.1
sqlparse==0.4.2
tzdata==2022.1

**settings.py > SECRET_KEY**
아래 링크에서 스크릿키 생성 후 작성
https://djecrety.ir/

## User Interface

**홈 화면**
![그림4](https://user-images.githubusercontent.com/86937253/209669718-7dcecbec-28a1-423d-81bc-fea2d7fafd4f.png)

**탐색 화면**
![그림5](https://user-images.githubusercontent.com/86937253/209669713-c1d0206a-1f08-4aa4-8981-f6481e291e4d.png)

**로그인 화면**
![그림6](https://user-images.githubusercontent.com/86937253/209669712-0bf12735-a148-4d87-9423-0fd3c05b535c.png)

**회원가입 화면**
![그림7](https://user-images.githubusercontent.com/86937253/209669711-c567bfc6-b420-4901-84f4-da6209aa332f.png)

**예술품 업로드 화면**
![그림8](https://user-images.githubusercontent.com/86937253/209669709-f0d80223-ac4c-480e-a6d8-3e28ef02ec21.png)

**개인 갤러리 화면**
![그림9](https://user-images.githubusercontent.com/86937253/209669706-d2d621f3-b638-421b-9ffd-6d081fe36f4b.png)

**예술품 디테일 화면**
![그림10](https://user-images.githubusercontent.com/86937253/209669699-6a0b2d94-47ed-447e-9c22-cc9c2bf9493f.png)

## Usage

    python manage.py runserver
