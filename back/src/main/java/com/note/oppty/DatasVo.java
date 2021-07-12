package com.note.oppty;

import java.sql.Timestamp;

import lombok.Data;
import lombok.ToString;

@Data
@ToString
public class DatasVo {
	private Integer oppty_data_no;
	private String userId;
	private String name;
	private String xstatusCd;
	private String sumWinProb;
	private String invstStgCd;
	private String optyType;
	private String marketClassCd;
	private String created;
	private String closeDt;
	private String bef1mSlgnAmt;
	private String circuitNum;
	private String code;
	private String text;
	private String slngAmt;
	private String purePrfit;
	private String minChDt;
	private String maxChDt;
	
	public DatasVo() {
		super();
	}

	public DatasVo(String userId, String name, String xstatusCd, String sumWinProb, String invstStgCd, String optyType,
			String marketClassCd, String created, String closeDt, String bef1mSlgnAmt, String circuitNum, String code,
			String text, String slngAmt, String purePrfit, String minChDt, String maxChDt) {
		super();
		this.userId = userId;
		this.name = name;
		this.xstatusCd = xstatusCd;
		this.sumWinProb = sumWinProb;
		this.invstStgCd = invstStgCd;
		this.optyType = optyType;
		this.marketClassCd = marketClassCd;
		this.created = created;
		this.closeDt = closeDt;
		this.bef1mSlgnAmt = bef1mSlgnAmt;
		this.circuitNum = circuitNum;
		this.code = code;
		this.text = text;
		this.slngAmt = slngAmt;
		this.purePrfit = purePrfit;
		this.minChDt = minChDt;
		this.maxChDt = maxChDt;
	}
	


	
}
