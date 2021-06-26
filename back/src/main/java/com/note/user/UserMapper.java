package com.note.user;

import java.util.List;

import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface UserMapper {
	public List<UserVo> selectUserList();
	public int signUp(UserVo user);
}
