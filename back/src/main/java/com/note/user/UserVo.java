package com.note.user;

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
		System.out.println("uservo");
	}
	
	public UserVo(String usersPassword, String usersName, String usersEmail) {
		this.usersPassword = usersPassword;
		this.usersName = usersName;
		this.usersEmail = usersEmail;
	}

	@Override
	public String toString() {
		return "UserVo [usersNo=" + usersNo + ", usersId=" + usersId + ", usersPassword=" + usersPassword + ", usersTel="
				+ usersTel + ", usersNickname=" + usersNickname + ", usersName=" + usersName
				+ ", usersEmail=" + usersEmail + "]";
	}
	
}
