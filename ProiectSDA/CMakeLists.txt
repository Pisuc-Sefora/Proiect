cmake_minimum_required(VERSION 3.22)
project(ProiectSDA)

set(CMAKE_CXX_STANDARD 14)

add_executable(ProiectSDA main.cpp Domain/User.cpp Domain/User.h Domain/Friendship.cpp Domain/Friendship.h Service/Service.cpp Service/Service.h UI/UI.cpp UI/UI.h RepositoryFile/Repository.cpp RepositoryFile/Repository.h Domain/Dictionary.h Domain/Node.h Domain/List.h)
