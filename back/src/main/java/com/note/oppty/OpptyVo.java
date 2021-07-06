package com.note.oppty;

import java.sql.Timestamp;

import com.note.user.UserVo;

import lombok.Data;
import lombok.ToString;

@Data
@ToString
public class OpptyVo {
	private String bef1mSlngAmt;
	private String circuitNum;
	private String invstStgCd;
	private String xoptyType;
	private String xtext;
	private String marketClassCd;
	private String createMonth;
	
	public OpptyVo() {
		System.out.println("opptyVo");
	}

	public OpptyVo(String bef1mSlngAmt, String circuitNum, String invstStgCd, String xoptyType, String xtext,
			String marketClassCd, String createMonth) {
		super();
		this.bef1mSlngAmt = bef1mSlngAmt;
		this.circuitNum = circuitNum;
		this.invstStgCd = invstStgCd;
		this.xoptyType = xoptyType;
		this.xtext = xtext;
		this.marketClassCd = marketClassCd;
		this.createMonth = createMonth;
	}
	
}
