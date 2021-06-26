package com.note.user;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;


@Service
public class UserService {

	@Autowired
	private UserMapper user;
	
	public List<UserVo> selectUserList() {
		return user.selectUserList();
	}
	
	public int signUp(UserVo uservo) {
		return user.signUp(uservo);
	}
}
