package com.note.oppty;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.util.List;

import org.apache.commons.exec.CommandLine;
import org.apache.commons.exec.DefaultExecutor;
import org.apache.commons.exec.PumpStreamHandler;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

import com.note.user.UserVo;


@Service
public class DatasService {
	
	@Autowired
	private DatasMapper datasmapper;
	
	public void insertDatas(DatasVo datas) {
		datasmapper.insertDatas(datas);
	}
	
	public List<DatasVo> loadAllData(){
		return datasmapper.loadAllData();
	}
}
