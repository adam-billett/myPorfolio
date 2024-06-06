package com.example.myportfolio.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.example.myportfolio.model.User;

public interface UserRepository extends JpaRepository<User, Integer> {

}
