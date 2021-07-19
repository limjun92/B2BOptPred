package com.note.oppty;

import java.sql.Timestamp;

import com.note.user.UserVo;

import lombok.Data;
import lombok.ToString;

@Data
@ToString
public class OpptyVo {
	private String name;
	private String type;
	private String opptyResultNo;
	private String opptyResult;
	private String usersId;
	private String newOrOld;
	private String bef1mSlngAmt;
	private String circuitNum;
	private String invstStgCd;
	private String optyType;
	private String text;
	private String marketClassCd;
	private String createMonth;
	private Timestamp joinDate;
	
	public OpptyVo() {
		System.out.println("opptyVo");
	}

	public OpptyVo(String name, String type, String bef1mSlngAmt, String circuitNum, String invstStgCd, String optyType, String text,
			String marketClassCd, String createMonth) {
		super();
		this.name = name;
		this.type = type;
		this.bef1mSlngAmt = bef1mSlngAmt;
		this.circuitNum = circuitNum;
		this.invstStgCd = invstStgCd;
		this.optyType = optyType;
		this.text = text;
		this.marketClassCd = marketClassCd;
		this.createMonth = createMonth;
	}

	public OpptyVo(String name, String type, String opptyResult, String usersId, String newOrOld, String bef1mSlngAmt, String circuitNum, String invstStgCd,
			String optyType, String text, String marketClassCd, String createMonth) {
		super();
		this.name = name;
		this.type = type; 
		this.opptyResult = opptyResult;
		this.usersId = usersId;
		this.newOrOld = newOrOld;
		this.bef1mSlngAmt = bef1mSlngAmt;
		this.circuitNum = circuitNum;
		this.invstStgCd = invstStgCd;
		this.optyType = optyType;
		this.text = text;
		this.marketClassCd = marketClassCd;
		this.createMonth = createMonth;
	}
	
}
