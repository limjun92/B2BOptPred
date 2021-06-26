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
	
	public UserVo(String usersId, String usersPassword, String usersTel, String usersNickname, String usersName,
			String usersEmail) {
		this.usersId = usersId;
		this.usersPassword = usersPassword;
		this.usersTel = usersTel;
		this.usersNickname = usersNickname;
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
