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
public class OpptyService {

	@Autowired
	private OpptyMapper opptymapper;

	public String getData(OpptyVo opptyVo) {
		String re = "";
		System.out.println("=============================");
		System.out.println("Python Call");
		String[] command = new String[9];
		command[0] = "python";
		// command[1] = "/Users/limju/OneDrive/바탕 화면/신입사원역량강화프로젝트/test.py";
		command[1] = "/Users/limju/OneDrive/바탕 화면/신입사원역량강화프로젝트/oppty_data.py";
		command[2] = opptyVo.getBef1mSlngAmt();
		command[3] = opptyVo.getCircuitNum();
		command[4] = opptyVo.getInvstStgCd();
		command[5] = opptyVo.getOptyType();
		command[6] = opptyVo.getText();
		command[7] = opptyVo.getMarketClassCd();
		command[8] = opptyVo.getCreateMonth();
		System.out.println();
		System.out.println(command[2]  +" " +  command[3] +" " + command[4] +" " +  command[5] +" " +  command[6] +" " +  command[7] +" " +  command[8]);
		try {
			re = execPython(command);
		} catch (Exception e) {
			e.printStackTrace();
		}
		
		
		// "제조/판매"가 없기 때문에 에러가 나는거다
//		System.out.println(re);
//		System.out.println(opptyVo.getName() + "?????????????????????");
		OpptyVo opptyResult = new OpptyVo(opptyVo.getName(), re, "준형", "기존", opptyVo.getBef1mSlngAmt(),
				opptyVo.getCircuitNum(), opptyVo.getInvstStgCd(), opptyVo.getOptyType(), opptyVo.getText(),
				opptyVo.getMarketClassCd(), opptyVo.getCreateMonth());
		
		opptymapper.getData(opptyResult);

		return re;
	}

	public static String execPython(String[] command) throws IOException, InterruptedException {
		CommandLine commandLine = CommandLine.parse(command[0]);
		for (int i = 1, n = command.length; i < n; i++) {
			commandLine.addArgument(command[i]);
		}

		ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
		PumpStreamHandler pumpStreamHandler = new PumpStreamHandler(outputStream);
		DefaultExecutor executor = new DefaultExecutor();
		executor.setStreamHandler(pumpStreamHandler);
		int result = executor.execute(commandLine);
		System.out.println("result: " + result);
		System.out.println("output: " + outputStream.toString());
		return outputStream.toString();

	}

	public List<OpptyVo> selectOpptyList() {
		return opptymapper.selectOpptyList();
	}
}
