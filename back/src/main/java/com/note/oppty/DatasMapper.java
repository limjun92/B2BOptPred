package com.note.oppty;

import java.util.List;

import org.apache.ibatis.annotations.Mapper;

import com.note.user.UserVo;

@Mapper
public interface DatasMapper {
	public void insertDatas(DatasVo datas);
	public List<DatasVo> loadAllData();
}
