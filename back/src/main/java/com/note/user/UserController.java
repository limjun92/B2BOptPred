package com.note.user;


import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;



@RestController
@RequestMapping("/getuser")
public class UserController {
	
	@Autowired
	private UserService User;
	
	@GetMapping("/get")
	public ResponseEntity<?> getUser() {
		List<UserVo> users = User.selectUserList();
		return ResponseEntity.status(HttpStatus.OK).body(users);
	}
	
	//회원가입
	@PostMapping("/register")
	public ResponseEntity<?> userEnroll(@RequestBody UserVo uservo) {
		System.out.println("================================================");
		System.out.println(uservo);
		int num = User.signUp(uservo);
		return ResponseEntity.status(HttpStatus.OK).body(num);
	}
}
