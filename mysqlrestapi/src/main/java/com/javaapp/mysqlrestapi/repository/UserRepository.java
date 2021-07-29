package com.javaapp.mysqlrestapi.repository;

import com.javaapp.mysqlrestapi.model.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * The interface User repository.
 *
 * @author Aman Jhagrolia
 */
@Repository
public interface UserRepository extends JpaRepository<User, Long> {}
