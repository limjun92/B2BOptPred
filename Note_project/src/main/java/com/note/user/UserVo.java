package com.note.user;

import java.sql.Date;
import java.sql.Timestamp;


import lombok.Data;
import lombok.ToString;

@Data
@ToString
public class UserVo {
	
	private Integer usersNo;
	private String usersId;
	private String usersPassword;
	private String usersTel;
	private String usersNickname;
	private String usersName;
	private String usersEmail;
	private Timestamp joinDate;
	private Timestamp modiDate;
	
	public UserVo() {
	
	}
	
	public UserVo(int usersNo){
		setUsersNo(usersNo);
	}
	
}
